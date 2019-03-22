# Simple API written in flask

Just another API written in flask, the URIS are:
- /events *get all events given*
- /events/:uuid *get the specific event*
- /reporters *get every reporter asigned to events*
- /reporters/events *get every event asigned to specific reporter*
- /types *get all the diferent event types*
- /types/events *get the all the events with a specific type*

## Options

- order_by: *you can pass uuid, name, reporter, comment, type, location or datetime and will return the events in the specific order*
- lat and lon: *will find every event with the specific location*
- start and stop: *will paginate the data*

## Examples

- https://events-sample.herokuapp.com/ *Heroku initial point*
- https://events-sample.herokuapp.com/events *get all the events*
- https://events-sample.herokuapp.com/events?order_by=name&lat=-99.06036355776905&lat=19.44700103604631&start=0&stop=10 *Use all filters*
- https://events-sample.herokuapp.com/reporters/events/Billi%20Waters *Get all the events cover by Billi Waters*
- https://events-sample.herokuapp.com/reporters/events/Billi%20Waters?order_by=type *same, but ordered*

*The filters work with every request that return events, like /types/events*
