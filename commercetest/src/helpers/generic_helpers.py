import random
import string
import logging as logger
from commercetest.src.helpers.config_helpers import get_base_url

def generate_random_email_and_password(domain=None, email_prefix=None):
    
    if not domain:
        domain = "testdomain.com"
    if not email_prefix:
        email_prefix = "testuser"

    random_email_string_length = 10
    ramdom_string = "".join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    email = email_prefix + "_" + ramdom_string + "@" + domain
    logger.info(f"Generated email: {email}")

    random_password_length = 10
    random_password = "".join(random.choices(string.ascii_letters, k=random_password_length))

    rondom_info = {"email": email, "password": random_password}

    return rondom_info

def generate_product_page_url_from_product_name(product_name):
    product_name_url = product_name.lower().replace(" ", "-")
    return f"{get_base_url()}/product/{product_name_url}/"