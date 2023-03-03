from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase
from django.utils.text import slugify
from django.utils.translation import gettext, gettext_lazy as _


class MyTag(TagBase):
    slug = models.SlugField(verbose_name=_('slug'), unique=True, max_length=100, allow_unicode=True)

    def slugify(self, tag, i=None):
        slug = slugify(tag, allow_unicode=True)
        if i:
            slug += f'_{i}'
        return slug

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
        app_label = 'taggit'


class TaggedItem(GenericTaggedItemBase):
    id = models.BigAutoField(primary_key=True)
    tag = models.ForeignKey(MyTag, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_items')


class Author(models.Model):
    DYNASTY = [
        ('上古', '上古'),
        ('夏', '夏'),
        ('商', '商'),
        ('西周', '西周'),
        ('东周', '东周'),
        ('春秋', '春秋'),
        ('战国', '战国'),
        ('秦', '秦'),
        ('西汉', '西汉'),
        ('东汉', '东汉'),
        ('魏', '魏'),
        ('蜀', '蜀'),
        ('吴', '吴'),
        ('西晋', '西晋'),
        ('东晋', '东晋'),
        ('南北朝', '南北朝'),
        ('隋', '隋'),
        ('唐', '唐'),
        ('五代', '五代'),
        ('北宋', '北宋'),
        ('南宋', '南宋'),
        ('元', '元'),
        ('明', '明'),
        ('清', '清'),
        ('民国', '民国'),
        ('现代', '现代'),
        ('当代', '当代'),
    ]

    NATION = [
        ('未知', '未知'),
        ('中国', '中国'),
        ('德国', '德国'),
        ('英国', '英国'),
        ('法国', '法国'),
        ('美国', '美国'),
        ('俄罗斯', '俄罗斯'),
        ('日本', '日本'),
        ('加拿大', '加拿大'),
        ('前苏联', '前苏联'),
        ('爱尔兰', '爱尔兰'),
        ('澳大利亚', '澳大利亚'),
        ('以色列', '以色列'),
        ('瑞士', '瑞士'),
        ('阿根廷', '阿根廷'),
        ('哥伦比亚', '哥伦比亚'),
        ('奥地利', '奥地利'),
        ('西班牙', '西班牙'),
        ('挪威', '挪威'),
        ('瑞典', '瑞典'),
        ('意大利', '意大利'),
        ('希腊', '希腊'),
        ('比利时', '比利时'),
        ('墨西哥', '墨西哥'),
        ('荷兰', '荷兰'),
        ('巴西', '巴西'),
        ('波兰', '波兰'),
        ('伊朗', '伊朗'),
        ('古巴', '古巴'),
        ('波斯', '波斯'),
        ('智利', '智利'),
        ('南非', '南非'),
        ('马来西亚', '马来西亚'),
        ('捷克', '捷克'),
        ('毛里求斯', '毛里求斯'),
        ('丹麦', '丹麦'),
    ]
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True, verbose_name='姓名')
    chinese_name = models.CharField(max_length=200, blank=True, unique=True, verbose_name='中文名')
    nation = models.CharField(max_length=100, choices=NATION, verbose_name='国籍')
    dynasty = models.CharField(max_length=100, blank=True, choices=DYNASTY, verbose_name='朝代')
    intro = models.TextField(max_length=1500, blank=True, verbose_name='简介')
    photo = models.ImageField(upload_to='image/authors/', verbose_name='相片', null=True, blank=True)

    class Meta:
        ordering = ['nation', 'dynasty', 'chinese_name', ]

    def __str__(self):
        author_name = self.name
        if self.chinese_name:
            author_name = self.chinese_name
        if self.dynasty:
            return "[{0}] {1}".format(self.dynasty, author_name)
        else:
            return "[{0}] {1}".format(self.nation, author_name)

    @property
    def full_name(self):
        author_name = self.name
        if self.chinese_name:
            author_name = self.chinese_name
        if self.dynasty:
            return "[{0}] {1}".format(self.dynasty, author_name)
        else:
            return "[{0}] {1}".format(self.nation, author_name)

    @property
    def books(self):
        return self.book_set.all()


class Bookshelf(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True, blank=True, default=None)
    total_book_count = models.IntegerField()
    total_set_count = models.IntegerField()

    @property
    def books(self):
        return self.book_set.all()

    @property
    def total_book_count(self):
        return sum([book.book_count for book in self.books])

    @property
    def total_set_count(self):
        return len(self.books)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, unique=True, verbose_name='名称')
    introduction = models.TextField(max_length=1500, blank=True, default=None, null=True, verbose_name='简介')

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, unique=True, verbose_name='名称')
    introduction = models.TextField(max_length=1500, blank=True, default=None, null=True, verbose_name='简介')

    def __str__(self):
        return self.name


class BookSeries(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, unique=True, verbose_name='名称')
    # books = models.ManyToManyField(Book)
    introduction = models.TextField(max_length=1500, blank=True, default=None, null=True, verbose_name='简介')

    def __str__(self):
        return self.name


class Book(models.Model):
    HARD_COVER = '精装'
    PAPER_COVER = '平装'
    BOX_SET = '盒装'
    WIRE_BOUND = '线装'
    BINDING_TYPE = [
        (HARD_COVER, HARD_COVER),
        (PAPER_COVER, PAPER_COVER),
        (BOX_SET, BOX_SET),
        (WIRE_BOUND, WIRE_BOUND),
    ]

    COATED_PAPER = '铜版纸'
    OFFSET_PAPER = '胶版纸'
    CHINA_PAPER = '宣纸'
    MUNKEN_PAPER = '轻型纸'
    PURE_QUALITY_PAPER = '纯质纸'
    WRITING_PAPER = '书写纸'
    ELEGANT_PAPER = '雅致纸'
    SPECIAL_PAPER = '特种纸'
    PAPER_TYPE = [
        (COATED_PAPER, COATED_PAPER),
        (OFFSET_PAPER, OFFSET_PAPER),
        (CHINA_PAPER, CHINA_PAPER),
        (MUNKEN_PAPER, MUNKEN_PAPER),
        (PURE_QUALITY_PAPER, PURE_QUALITY_PAPER),
        (WRITING_PAPER, WRITING_PAPER),
        (ELEGANT_PAPER, ELEGANT_PAPER),
        (SPECIAL_PAPER, SPECIAL_PAPER),
    ]

    CHINESE = '中文'
    TRADITIONAL_CHINESE = '繁体中文'
    ENGLISH = '英文'
    CHINESE_ENGLISH = '中文/英文'
    JANPANESE = '日文'
    LANGUAGES = [
        (CHINESE, CHINESE),
        (TRADITIONAL_CHINESE, TRADITIONAL_CHINESE),
        (ENGLISH, ENGLISH),
        (CHINESE_ENGLISH, CHINESE_ENGLISH),
        (JANPANESE, JANPANESE),
    ]

    HORIZONTAL = '横排'
    VERTICAL = '竖排'
    COMPOSE_TYPES = [
        (HORIZONTAL, HORIZONTAL),
        (VERTICAL, VERTICAL)
    ]

    NOT_READ = '未读'
    READING = '在读'
    FINISHED = '已读'
    READ_STATE = [
        (NOT_READ, NOT_READ),
        (READING, READING),
        (FINISHED, FINISHED)
    ]

    SCORES = [(i, i) for i in range(11)]

    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=30, unique=False)
    chinese_name = models.CharField(max_length=200, blank=True, default=None, verbose_name='中文译名', null=True)
    original_name = models.CharField(max_length=200, verbose_name='名称')
    authors = models.ManyToManyField(Author, blank=True)
    translator = models.CharField(max_length=100, blank=True, default=None, null=True, verbose_name='翻译/编纂/整理')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name='出版社', default=None,
                                  related_name='books', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='品牌', default=None, related_name='books',
                              blank=True, null=True)
    publish_date = models.DateField(verbose_name='出版日期', blank=True)
    book_series = models.ForeignKey(BookSeries, on_delete=models.CASCADE, verbose_name='丛书', default=None,
                                    related_name='books', blank=True, null=True)
    binding_type = models.CharField(max_length=20, choices=BINDING_TYPE, verbose_name='装帧', default=HARD_COVER)
    paper_type = models.CharField(max_length=20, blank=True, default=OFFSET_PAPER, choices=PAPER_TYPE,
                                  verbose_name='用纸')
    pages = models.IntegerField(verbose_name='页数', default=1)
    book_count = models.IntegerField(verbose_name='套装数量', default=1)
    language = models.CharField(max_length=30, choices=LANGUAGES, verbose_name='正文语种', default=CHINESE)
    compose_type = models.CharField(max_length=10, choices=COMPOSE_TYPES, verbose_name='排版', default=HORIZONTAL)
    price = models.FloatField(verbose_name='定价', blank=True)
    purchase_price = models.FloatField(verbose_name='购入价格', blank=True)
    purchase_date = models.DateField(verbose_name='购入日期', blank=True)
    thumb_image = models.ImageField(upload_to='image/books/', verbose_name='缩略图', blank=True, default=None)
    link = models.CharField(max_length=200, blank=True, default=None, verbose_name='商品链接', null=True)
    category = models.CharField(max_length=100, verbose_name='分类', blank=True)
    bookshelf = models.ForeignKey(Bookshelf, on_delete=models.CASCADE, default=1, verbose_name='所在书架')
    read_state = models.CharField(max_length=20, choices=READ_STATE, verbose_name='阅读状态', default=NOT_READ)
    introduction = models.TextField(max_length=5000, blank=True, default=None, null=True, verbose_name='简介')
    registered = models.CharField(max_length=20, choices=[('Yes', 'Yes'), ('No', 'No')], verbose_name="登记状态",
                                  default='No')
    edition = models.CharField(max_length=50, verbose_name='版次', default=None, blank=True, null=True)
    print = models.CharField(max_length=30, verbose_name='印次', default=None, blank=True, null=True)
    printed_number = models.CharField(max_length=30, verbose_name='印数', default=None, blank=True, null=True)
    my_score = models.IntegerField(choices=SCORES, verbose_name='我的评分', default=None, null=True, blank=True)
    douban_score = models.IntegerField(verbose_name='豆瓣评分', default=0, null=True, blank=True)
    my_comments = models.TextField(max_length=1500, blank=True, default=None, null=True, verbose_name='我的点评')
    tags = TaggableManager(blank=True, through=TaggedItem)

    class Meta:
        ordering = ['chinese_name', ]

    def __str__(self):
        postfix = ''
        author_str_list = self.get_authors_display()
        if author_str_list:
            postfix = author_str_list[0]
        else:
            postfix = self.isbn
        return f'{self.original_name} | {self.chinese_name} |{postfix}'

    def get_authors_display(self):
        author_list = []
        for author in self.authors.all():
            author_list.append(str(author))
        return author_list

    @property
    def authors_str(self):
        return '\n'.join(self.authors)

    @property
    def num_of_comments(self):
        return Comment.objects.filter(book=self).count()


class BookCollection(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, unique=True, verbose_name='名称')
    books = models.ManyToManyField(Book)
    introduction = models.TextField(max_length=1500, blank=True, default=None, null=True, verbose_name='简介')

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
    The model used to store the comments.
    """
    id = models.BigAutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.book)


class ReadingPlan(models.Model):
    """
    The model used to store the reading plans
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="计划名")
    description = models.TextField(verbose_name="计划详情")
    start_date = models.DateField()
    end_date = models.DateField()
    books = models.ManyToManyField(Book)

    def complete_ratio(self):
        completed_count = sum([book.book_count for book in self.books.all() if book.read_state == Book.FINISHED])
        planed_count = sum([book.book_count for book in self.books.all()])
        return f'{round(completed_count / planed_count, 2) * 100}%'

    complete_ratio.short_description = '完成率'


class AuthorBookRelationship(models.Model):
    """
    The model used to store the relationship between authors and books
    """
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')


class BookImage(models.Model):
    """
    The model for images
    """
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to='image/books/')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book'),
