# stinky-beer
 AstroYeast Main Repository



## DB Migrate
```
docker-compose run web python manage.py migrate
```
## DB Update Models

```
docker-compose run web python manage.py makemigrations
```

## NEXT.js Dashboard

```
cd next-dashboard
yarn install && yarn run dev
```