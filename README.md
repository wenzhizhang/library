# library
This App is used to manage the books I own
Restful API is provided to manage the books, authors, producers and so on.

# Preview
- Book list view

    ![Book List View](study/media/image/screenshots/BookList.png)

- Book eetails view

    ![Book Details View](study/media/image/screenshots/BookDetails.png)

- Author and his/her books

    ![Author View](study/media/image/screenshots/AuthorView.png)

- Publisher and its published books

    ![Publisher View](study/media/image/screenshots/PublisherView.png)

- Book series view

    ![Book Series View](study/media/image/screenshots/BookSeriesView.png)

- Reading plan
    ![Reading Plan](study/media/image/screenshots/ReadingPlan.png)

# Usage
- Running on windows.  
    ```bash
    python manage.py runserver 
    ```
- Running in WSL with uWSGI and NGINX.  
    ```bash
    uwsgi --ini config/uwsgi_wsl.ini
    ```
- Running in Docker container.  
    ```bash
    # Build docker conainer.
    docker build -t library .
    # Run with docker container.
    docker run -it -p 8080:8080 -p 8443:8443 -e DJANGO_SUPERUSER_USERNAME=admin -e DJANGO_SUPERUSER_PASSWORD=******** -e DJANGO_SUPERUSER_EMAIL=admin@example.com library
    ```