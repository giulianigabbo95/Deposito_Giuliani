'''
Esercizi PT. 1
'''

-- Estrai i nomi (first_name) e i cognomi (last_name) di tutti gli attori presenti nella tabella actor.
-- Rinomina le colonne come "Nome" e "Cognome" perren dere il report più leggibile.
SELECT 
	first_name AS Nome, 
    last_name AS Cognome 
    FROM 
		actor;

-- Trova tutti i titoli dei film che hanno un rating uguale a 'G' (General Audiences).
SELECT 
	title, 
    rating 
    FROM 
		film 
		WHERE 
			rating = "G";

-- Trova tutti i clienti nella tabella customer il cui nome inizia con la lettera "A" e il cognome finisce con la lettera "S".
SELECT 
	customer_id 
    FROM 
		customer 
		WHERE 
			first_name LIKE "A%" AND 
            last_name LIKE "%s";

-- Seleziona i film che hanno una durata (length) superiore a 150 minuti E un costo di noleggio (rental_rate) inferiore a 1.00$.
SELECT 
	film_id 
	FROM 
		film 
		WHERE 
			length > 150 AND 
            rental_rate < 1.00;


       
'''
Esercizi PT. 2
'''           
-- Mostra i 10 film più lunghi presenti nel database, ordinandoli dal più lungo al più corto.
SELECT 
	title, 
	film_id,
	length 
	FROM 
		film 
		ORDER BY 
			length DESC;

-- Qual è il prezzo medio di noleggio (rental_rate) di tutti i film?
-- Rinomina il risultato come "Prezzo_Medio_Noleggio".
SELECT 
	AVG(rental_rate) AS Prezzo_Medio_Noleggio 
	FROM 
		film;

-- Nella tabella film, conta quanti film ci sono per ogni durata di noleggio (rental_duration).
SELECT 
	rental_duration, 
	COUNT(film_id) 
	FROM 
		film 
		GROUP BY 
			rental_duration;

-- Vai nella tabella payment e conta quanti pagamenti ha registrato ogni staff_id.
SELECT 
	staff_id,
	COUNT(payment_id) 
	FROM 
		payment
		GROUP BY 
			staff_id;

-- Per ogni customer_id nella tabella payment, mostra il pagamento più alto (MAX) e quello più basso (MIN) che abbiano mai effettuato.
SELECT 
	customer_id, 
	MAX(amount), 
	MIN(amount) 
	FROM 
		payment 
		GROUP BY 
			customer_id;