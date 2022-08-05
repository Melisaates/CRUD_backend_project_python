INSERT INTO dealer (id,dealer_name,dealer_code,neighborhood_id,district_id,city_id,working_hours,is_active,qrcode,info,image,payment_info,table_is_active,reservation_is_active,marketplaces_is_active)
VALUES (:id,:dealer_name,:dealer_code,:neighborhood_id,:district_id,:city_id,:working_hours,:is_active,:qrcode,:info,:image,:payment_info,:table_is_active,:reservation_is_active,:marketplaces_is_active) returning id;


