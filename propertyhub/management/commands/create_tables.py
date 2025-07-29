from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = "Create tables using raw SQL for users, properties, requirements, and reviews."

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id SERIAL PRIMARY KEY,
                    username VARCHAR(255),
                    email VARCHAR(255),
                    phone_number VARCHAR(20),
                    whatsapp VARCHAR(20),
                    contact_details VARCHAR(255),
                    profile_photo TEXT,
                    user_type VARCHAR(50),
                    joined_date TIMESTAMP,
                    ratings FLOAT,
                    bio TEXT,
                    password VARCHAR(128)      
                );

                CREATE TABLE IF NOT EXISTS properties (
                    property_id SERIAL PRIMARY KEY,
                    title VARCHAR(255),
                    property_type VARCHAR(30),
                    location VARCHAR(150)
                    pincode VARCHAR(10),
                    monthly_rent DECIMAL(10, 2),
                    deposit_amount DECIMAL(10, 2),
                    photos TEXT,
                    property_description TEXT,
                    listed_date_time DATETIME,
                    listed_by_user_id INT,
                    FOREIGN KEY (listed_by_user_id) REFERENCES users(user_id)
                );

                CREATE TABLE IF NOT EXISTS requirements (
                    requirement_id SERIAL PRIMARY KEY,
                    user_id INT,
                    preferred_city VARCHAR(100),
                    preferred_locality VARCHAR(100),
                    property_type VARCHAR(100),
                    budget_min DECIMAL(10, 2),
                    budget_max DECIMAL(10, 2),
                    move_in_date DATE,
                    amenities_required TEXT,
                    other_preferences TEXT,
                    FOREIGN KEY (user_id) REFERENCES users(user_id)
                );

                CREATE TABLE IF NOT EXISTS reviews (
                    review_id SERIAL PRIMARY KEY,
                    reviewer_user_id INT,
                    reviewed_user_id INT,
                    rating INT,
                    review_text TEXT,
                    date TIMESTAMP,
                    FOREIGN KEY (reviewer_user_id) REFERENCES users(user_id),
                    FOREIGN KEY (reviewed_user_id) REFERENCES users(user_id)
                );
            """)

        self.stdout.write(self.style.SUCCESS("All tables formed successfully using raw SQL."))


#* property_type VARCHAR(30),
#* location
#* monthly_rent DECIMAL(10, 2),
#* contact number,
# deposit_amount DECIMAL(10, 2),
# available_from DATE,
# amenities TEXT,
#* photos TEXT,
# property_description TEXT,
# number_of_bedrooms INT,
# number_of_bathrooms INT,
#* date TIMESTAMP
#* FOREIGN KEY (user_id) REFERENCES users(user_id)