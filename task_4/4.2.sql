select cus.name, cit.name from customers as cus
left join cities cit on cus.city_id = cit.id;
