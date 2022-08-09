SELECT (SELECT jsonb_agg(c)
        from (SELECT d.id,
                     d.dealer_name,
                     d.dealer_code,
                     d.neighborhood_id,
                     d.district_id,
                     d.city_id,
                     d.working_hours,
                     d.is_active,
                     d.qrcode,
                     d.info,
                     d.image,
                     d.payment_info,
                     d.table_is_active,
                     d.reservation_is_active,
                     d.marketplaces_is_active
              FROM dealer d
                       inner join brand b on b.id = d.brand_id
              WHERE b.id = :brand_id) c)   as dealer_properties,
       (select jsonb_agg(g)
        from (select p.id,
                     p.is_active,
                     p.is_sell,
                     p.product_code,
                     p.make_time,
                     p.colorie,
                     p.tags,
                     p.product_type_id,
                     p.dealer_id,
                     p.just_restaurant

              FROM product p
                       inner join dealer d on d.id = p.dealer_id
                       inner join brand b on b.id = d.brand_id
              WHERE b.id = :brand_id) g) as product_properties


FROM brand b
         INNER JOIN dealer d ON d.brand_id = b.id
WHERE b.id = :brand_id


