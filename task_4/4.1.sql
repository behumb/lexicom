select cus.name, cit.name from customers as cus
full join cities cit on cus.city_id = cit.id;