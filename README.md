#Simple API written in flask

Just another API written in flask, the URIS are:
- /events *get all events given*
- /events/:uuid *get the specific event*
- /reporters *get every reporter asigned to events*
- /reporters/events *get every event asigned to specific reporter*
- /types *get all the diferent event types*
- /types/events *get the all the events with a specific type*

##Options

- order_by: *you can pass uuid, name, reporter, comment, type, location or datetime and will return the events in the specific order*
- lat and lon: *will find every event with the specific location*
- start and stop: *will paginate the data*

##Examples

- http://0.0.0.0:5000/events: *get all the events*
- http://0.0.0.0:5000/events?order_by=name&lat=-99.06036355776905&lat=19.44700103604631&start=0&stop=10: *Use all filters*

*The filters work with every request that return events, like /types/events*
