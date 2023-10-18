Sailor training center: Captain's coffee
====================================

## Task
Ahoy, deck cadet,

your task is to prepare good coffee for captain. As a cadet, you are prohibited from going to the captain's cabin, so you will have to solve the task remotely. Good news is that the coffee maker in captain's cabin is online and can be managed via API.

May you have fair winds and following seas!

Coffee maker API is available at http://coffee-maker.cns-jv.tcc.

## Solution
I've opened the link in browser. Web server return this:

	{"status":"Coffemaker ready","msg":"Visit /docs for documentation"}

So I changed URL to: http://coffee-maker.cns-jv.tcc/docs
There is swagger UI with API documentation and posibility to execute endpoints. So execute coffeeMenu return this:

	{
	  "Menu": [
	    {
	      "drink_name": "Espresso",
	      "drink_id": 456597044
	    },
	    {
	      "drink_name": "Lungo",
	      "drink_id": 354005463
	    },
	    {
	      "drink_name": "Capuccino",
	      "drink_id": 234357596
	    },
	    {
	      "drink_name": "Naval Espresso with rum",
	      "drink_id": 501176144
	    }
	  ]
	}

Now we execute POST /makeCoffee and fill drink_id 501176144 (Naval Espresso with rum). And we have solution:

	{
	  "message": "Your Naval Espresso with rum is ready for pickup",
	  "validation_code": "Use this validation code FLAG{ccLH-dsaz-4kFA-P7GC}"
	}