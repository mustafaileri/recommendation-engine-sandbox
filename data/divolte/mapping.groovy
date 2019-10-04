mapping {
	map partyId() onto 'click_stream_cookie_id'
  	map eventParameter('click_stream_cookie_id') onto 'click_stream_cookie_id'
  	map eventType() onto 'event_name'
  	map eventParameter('item_id') onto 'item_id'
  	map timestamp() onto 'event_date'
  	map location() onto 'url'
  	map remoteHost() onto 'client_ip'
}