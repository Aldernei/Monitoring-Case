

SELECT * FROM checkout_1 WHERE time = '08h'


INSERT INTO checkout_1 (time, today, yesterday, same_day_last_week, avg_last_week, avg_last_month)
VALUES ('09h', 20, 10, 15, 18.5, 19.2)


UPDATE checkout_1 SET today = 30 WHERE time = '10h'


DELETE FROM checkout_1 WHERE time = '05h'
