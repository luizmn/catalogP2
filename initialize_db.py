from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Product, User

engine = create_engine('sqlite:///productscatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="John Rusty", email="rustyjohn@products.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Add suspension category
category1 = Category(user_id=1, name="Suspension")

session.add(category1)
session.commit()

# Add items in suspension category
product1 = Product(user_id=1, name="Fox Front Shocks", description="Fox Shocks are used in off-road vehicles. Comfort and endurance in all-terrain.",
                     price="$250.99", category=category1)
session.add(product1)
session.commit()

product2 = Product(user_id=1, name="Coil Springs", description="Restore OEM-standard handling and smoother ride to your vehicle.",
                     price="$45.00", category=category1)
session.add(product2)
session.commit()

# Add lightning category
category2 = Category(user_id=1, name="Lightning")

session.add(category2)
session.commit()

# Add items in suspension category
product1 = Product(user_id=1, name="H7 Led Bulb", description="Each bulb has 2 pcs of high power COB chips made in Taiwan, perfect light pattern without dark spot,6000-6500K",
                     price="$20.98", category=category2)
session.add(product1)
session.commit()

product2 = Product(user_id=1, name="Led Light Bar", description="The appropriate mix and match of spot beams and flood beams provides a long irradiation distance and broad view.",
                     price="$27.41", category=category2)
session.add(product2)
session.commit()

# Add lights category
category3 = Category(user_id=1, name="Brake System")

session.add(category3)
session.commit()

# Add lights category
category4 = Category(user_id=1, name="Tires")

session.add(category4)
session.commit()

print("added initial categories and products!")

