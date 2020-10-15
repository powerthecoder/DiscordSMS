
const msgInfo = require('./msg_sent.json')

const accountSid = 'ACCOUNTSID';
const authToken = 'AUTHTOKEN';
const client = require('twilio')(accountSid, authToken);

const msg = msgInfo.message_s + ' Sent From: ' + msgInfo.sent_from

client.messages
  .create({
     body: msg,
     from: '+1TWILLOPHONE',
     to: '+1YOURPHONE'
   })
  .then(message => console.log(message.sid));
