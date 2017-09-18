echo "destroying everything";
docker-compose down;

echo "Building images";
docker-compose build;

echo "initializing DB";
docker-compose up -d db;
sleep 10;

echo "starting the rest of the conatainers";
docker-compose up -d;

echo "Creating databas tables";
docker-compose exec api python manage.py makemigrations;
docker-compose exec api python manage.py migrate;

echo "installing fixtures";
docker-compose exec api python manage.py loaddata;

echo "Done your docker containers are up and running";