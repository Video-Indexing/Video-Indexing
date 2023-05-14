
const nodemailer = require('nodemailer');

const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.VIP_MAIL_USR, 
      pass: process.env.VIP_MAIL_PSW 
    }
  });

function sendMailToClient(clientMail, userName, vidName){
    let mailOptions = {
        from: process.env.VIP_MAIL_USR, 
        to: clientMail, 
        subject: 'Upload mail finished', // Subject line
        text: `Hi ${userName},\n\nYour upload of ${vidName} is finished\n\nThank you,\n\nVIP team`, // plain text body
      };
    
    transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
        console.error(error);
        console.log('error: An error occurred while sending the email');
    } else {
        console.log('Message sent: %s', info.messageId);
    }
    });
}

module.exports = { sendMailToClient };
