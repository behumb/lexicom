select cit.name, cus.name from customers as cus
right join cities cit on cus.city_id = cit.id;