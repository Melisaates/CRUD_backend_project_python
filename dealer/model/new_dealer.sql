SELECT *,
       (select json_build_object(
                       'price',
                       coalesce(pp.price, pdp.price),
                       'product_price', pp.id,
                       'product_dealer_price', pdp.id) as price
        from product_price pp
                 inner join product_dealer_price pdp on pp.id = pdp.product_price_id
                 inner join dealer d on d.id = pdp.dealer_id
        where d.city_id = :city_id)
FROM dealer d
         INNER JOIN city c ON d.city_id = c.id
WHERE d.city_id = :city_id;


--select jsonb_agg()