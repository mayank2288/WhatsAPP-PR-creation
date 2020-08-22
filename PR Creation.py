#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client 
import requests

account_sid = 'xxxxxxxxb987613cb5exxxxxxxxx' 
auth_token = 'xxxxxxx622c988d623fxxxxxxx' 
client = Client(account_sid, auth_token) 

body ="""How Can I help you?\n 1.Perform Inventory Transaction (Format: "Sr.no" ItemNumber Quantity UOM)\n\n 
2.Show me Item availability (Format: "Sr.no" ItemNumber) \n\n
3.Create Requisition Order -Non Catalog (Format: "Sr.no" Item-Description Price Quantity)"""


message = client.messages.create( 
                              from_='whatsapp:+11111111111',  
                              body= body,      
                              to='whatsapp:+22222222222' 
                                )


url3="https://efmr-dev1.fa.us6.oraclecloud.com/fscmService/PurchaseRequestService?WSDL"

headers1 = {'content-type': 'text/xml','Authorization': 'Basic xxxxxxxxxxxx0aXMuY29xxxxxxxxxxxbx='}

body_pr = """<soapenv:Envelope xmlns:pur="http://xmlns.oracle.com/apps/prc/po/editDocument/purchaseRequestService/" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tns="http://xmlns.oracle.com/apps/prc/po/editDocument/purchaseRequestService/types/" xmlns:typ="http://xmlns.oracle.com/apps/prc/po/editDocument/purchaseRequestService/types/">
   <soapenv:Body>
      <tns:createRequisition xmlns:ns1="http://xmlns.oracle.com/adf/svc/errors/" xmlns:ns2="http://xmlns.oracle.com/apps/prc/po/editDocument/purchaseRequestService/" xmlns:ns3="http://xmlns.oracle.com/adf/svc/types/" xmlns:ns4="commonj.sdo/xml" xmlns:ns5="commonj.sdo/java" xmlns:ns6="commonj.sdo" xmlns:nxsd="http://xmlns.oracle.com/pcbpel/nxsd">
         <tns:interfaceSourceCode>WhatsApp</tns:interfaceSourceCode>
         <tns:requisitioningBUName>OTIS HONG KONG</tns:requisitioningBUName>
         <tns:groupBy>SUPPLIER</tns:groupBy>
         <tns:initiateApprovalAfterRequisitionImport>Y</tns:initiateApprovalAfterRequisitionImport>
         <tns:maximumBatchSize>1</tns:maximumBatchSize>
         <tns:purchaseRequestPayload>
            <ns2:RequisitioningBUName>OTIS HONG KONG</ns2:RequisitioningBUName>
            <ns2:Attribute1>Service Without Work Order-500</ns2:Attribute1>
            <ns2:Attribute2>51149942_00000000</ns2:Attribute2>
            
            <ns2:Attribute10>10619144</ns2:Attribute10>
                  
            <ns2:DocumentStatusCode>INCOMPLETE</ns2:DocumentStatusCode>
            <ns2:PreparerEmail>mayank.pande@otis.com</ns2:PreparerEmail>
            <ns2:ExternallyManagedFlag>False</ns2:ExternallyManagedFlag>
           
            <ns2:PurchaseRequestInputReqLineInterface>
                
              <ns2:ProcurementBUName>OTIS HONG KONG</ns2:ProcurementBUName>
              <ns2:Attribute1>249762</ns2:Attribute1>

              <ns2:ItemDescription>{0}</ns2:ItemDescription>

               <ns2:DeliverToLocationCode>Otis Hong Kong</ns2:DeliverToLocationCode>
              <ns2:SupplierName>Otis Elevator (China) Co. (OECC)</ns2:SupplierName>
               <ns2:SupplierSiteName>23929444</ns2:SupplierSiteName>
              <ns2:UnitOfMeasure>EA</ns2:UnitOfMeasure>
               <ns2:CurrencyCode>HKD</ns2:CurrencyCode>
               <ns2:LineType>Goods</ns2:LineType>
              <ns2:RequesterEmail>mayank.pande@otis.com</ns2:RequesterEmail>
              <ns2:Price>{1}</ns2:Price>
               <ns2:Attribute5>Y</ns2:Attribute5>
               <pur:RequestedDeliveryDate>2020-12-09</pur:RequestedDeliveryDate>
               <ns2:CategoryName>OTIS Purchasing</ns2:CategoryName>
               <ns2:DestinationTypeCode>EXPENSE</ns2:DestinationTypeCode>
               <ns2:Quantity>{2}</ns2:Quantity>
               <ns2:RateType>Corporate</ns2:RateType>               
               <ns2:PurchaseRequestInputReqDistInterface>
                  <ns2:ChargeAccountSegment1>500</ns2:ChargeAccountSegment1>
                  <ns2:ChargeAccountSegment2>000000</ns2:ChargeAccountSegment2>
                  <ns2:ChargeAccountSegment3>00000000</ns2:ChargeAccountSegment3>
                  <ns2:ChargeAccountSegment4>000000</ns2:ChargeAccountSegment4>
                  <ns2:ChargeAccountSegment5>000000</ns2:ChargeAccountSegment5>
                  <ns2:ChargeAccountSegment6>000000</ns2:ChargeAccountSegment6>
                  <ns2:ChargeAccountSegment7>000000</ns2:ChargeAccountSegment7>
                  <ns2:ChargeAccountSegment8>000000</ns2:ChargeAccountSegment8>
                  <ns2:Percent>100</ns2:Percent>
               </ns2:PurchaseRequestInputReqDistInterface>
            </ns2:PurchaseRequestInputReqLineInterface>
         </tns:purchaseRequestPayload>
      </tns:createRequisition>
   </soapenv:Body>
</soapenv:Envelope>
"""
    

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a message."""
    # Fetch the message
    msg = request.form.get('Body')
    x = tuple(msg.split())
    a = x[0]
    
    if a == "1":
        b = x[1]
        c = x[2]
        d = x[3]
        f = item.format(b,c,d)
        fpayload = '{"transactionLines": [' + payload + f + '}]}'
        print(fpayload)
        response = requests.post(url,headers=headers,data = fpayload)
        az = response.json()
        msg = str(az['ReturnStatus'])

        print(msg + msg1)
        
    elif a == "2":
        b = x[1]
        #c = x[2]
        #d = x[3]
        f = item1.format(b)
        fpayload1 = payload1 + f + "}"
        print(fpayload1)
        response = requests.request("POST", url1, headers=headers, data = fpayload1)
        jsres = response.json()
        jres1 = "Item {} has Quantity {} {}".format(jsres['ItemNumber'],jsres['QuantityOnhand'],jsres['PrimaryUnitOfMeasure'])
        #msg1 = sendname()
        msg = jres1
    elif a == "3":
        b = x[1]
        c = x[2]
        d = x[3]
        body_pr1 = body_pr.format(b,c,d)
                            
        response = requests.post(url3,data=body_pr1,headers=headers1)
        r1 = response.text
        #print(a)
        result = r1.split("RequisitionNumber>",1)[1]
        prnum = result.split("</ns0:RequisitionNumber>",1)[0]
        msg = "PR created: " + prnum
    else:
        msg = "Please provide proper format"
    
    # Create reply
    
    resp = MessagingResponse()
    resp.message(msg)
           
    return str(resp)

if __name__ == "__main__":
    app.run(debug=False)



    

