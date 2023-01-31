{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Sid":"AddPerm",
      "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:s3:::s3.policy.test/*"]
    }
  ]
}
 
 
    import PyPDF2
    from PyPDF2 import PdfFileReader
    
    # Open the PDF file
    pdf_file = open(r"C:\\Users\\file.pdf", 'rb')
    pdf_reader = PdfFileReader(pdf_file)
    
    # Iterate through each page
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        xObject = page['/Resources']['/XObject'].getObject()
    
        # Iterate through each image on the page
        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                data = xObject[obj].getData()
                # You can now save the image data to a file
                with open(f'C:\\Users\\filepath\{obj}.jpg', 'wb') as img_file:
                    img_file.write(data)
    
    # Close the PDF file
    pdf_file.close()

