# Hur man triggera våra alarm
- Vi har satt upp så att om man få en 5xx error över 1 minut så kommer det triggera i våra alarm.

- För att kunna triggera våra alarm, har vi en route till våra app: https://jofb21.me/trigger-500. Om man refresha några gånger under 1 minut (för att simulera en riktigt 5xx problem) så kommer det dyk upp i http://52.138.179.192:9090/classic/alerts.

Länk till rules:
http://52.138.179.192:9090/classic/rules