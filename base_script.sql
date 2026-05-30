# Выводим список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).

SELECT
  c.login AS login,
  COUNT(o.id) AS "delivery_cnt"
FROM
  "Couriers" AS с
LEFT JOIN
  "Orders" AS o 
ON c.id = o."courierId"
WHERE
  o."inDelivery" = true
GROUP BY
  c.login;


# Выводим все трекеры заказов и их статусы.

SELECT
  track,
  CASE
    WHEN finished = true THEN 2
    WHEN cancelled = true THEN -1
    WHEN "inDelivery" = true THEN 1
  ELSE 0 
  END AS status_order
FROM
  "Orders";
