# Anime List Application

This application allows users to view and manage a list of anime using data pulled from the MyAnimeList API.

## Setup

1. Clone the repository.
2. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Set up the database:
    ```
    flask db init
    flask db migrate
    flask db upgrade
    ```
4. Run the application:
    ```
    flask run
    ```

## Routes

- `/` - Shows a list of anime.
- `/anime/<int:anime_id>` - Shows the details of a specific anime.
- `/api/anime` - Pulls anime data from the MyAnimeList API.

## Configuration

- Update your database URI in `app.py`.
- Add your MyAnimeList API token in `app.py`.

## Dependencies

- Flask
- Flask-SQLAlchemy
- Requests
