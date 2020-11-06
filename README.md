# Send instant e-mail from any Apps using REST API endpoint deployed using OCI API Gateway, Functions and Email Delivery.

ex:

$ curl -i -X GET https://ktk2mm4pinz5dm.apigateway.us-ashburn-1.oci.customer-oci.com/v1/func1 -d '{"senderAddress" : "sender@yourdomain.com", "senderName" : "OCI Fn/APIGW", "recipientAddress" : "recipient@therdomain.com", "emailSubject" : "TestMail from OCI Fn/APIGW"}'
