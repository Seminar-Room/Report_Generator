from reportlab.lib import colors
from reportlab.platypus import  Paragraph, Frame, KeepInFrame, Spacer, PageBreak
from reportlab.lib.styles import  ParagraphStyle 
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from PIL import Image

#alignment 
from reportlab.lib.enums import TA_JUSTIFY

#bar chart
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
import os
import zipfile
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def register_fonts():
    font_path1 = r'testing_details/fonts/Poppins-Regular.ttf'
    pdfmetrics.registerFont(TTFont('Poppins-Regular', font_path1))

    font_path2 = r'testing_details/fonts/Poppins-Bold.ttf'
    pdfmetrics.registerFont(TTFont('Poppins-Bold', font_path2))


register_fonts()

# Create a custom image resizer for drawing the new images
def image_resizer(photo,image_width,image_height):
            # Define the dimensions of the area you want to fill
            photo_width =image_width
            photo_height = image_height
            
            # Open the image and get its dimensions
            img = Image.open(photo)
            img_width, img_height = img.size
            # Calculate the aspect ratio
            aspect_ratio = img_width / img_height

            # Determine whether to adjust width or height based on the aspect ratio
            if photo_width / aspect_ratio > photo_height:
                photo_width = photo_height * aspect_ratio
            else:
                photo_height = photo_width / aspect_ratio

            return photo_width , photo_height



page_width=210*mm
class iip_reports:
    
    def __init__(self, pdf_canvas):
        self.canvas = pdf_canvas

    def add_background_template(self):
        # Add a page break before the index content
        self.canvas.showPage()
        
        #addind back ground template
        background_path = 'testing_details/Feedback FSD - DGI.png'
        # Draw the background image
        self.canvas.drawImage(background_path, 0, 0, width=210*mm, height=297*mm)

    ########################################################## PAGE_1 ########################################################
    def add_coverpage(self,event_name, college_name, college_logo):
        #coverpage
        # Add a background image of your choice as the certificate template
        background_path = 'testing_details/1.png'
        # Draw the background image
        self.canvas.drawImage(background_path, 0, 0, width=210*mm, height=297*mm)

        #adding event name,images of college logo and seminarroom logo
        # Create a Frame for the text box
        frame_width = 190*mm # Adjust the width as needed
        frame_height = 210 * mm  # Adjust the height as needed
        frame_x = (page_width - frame_width) / 2 
        frame_y =30* mm
        frame = Frame(frame_x, frame_y, frame_width, frame_height, showBoundary=0)  # Set showBoundary=1 for debugging
       
        # Define styles for different parts of the paragraph
        Bold_Style1 = ParagraphStyle(
                "Bold_Style1",
                fontSize=30,
                fontName="Poppins-Bold",
                textColor=colors.HexColor("#613880"),
                alignment=1, # 1 center align
                leading=8*mm
            )
        Bold_Style2 = ParagraphStyle(
                "Bold_Style2",
                fontSize=30,
                fontName="Poppins-Bold",
                textColor=colors.HexColor("#612880"),
                alignment=1,
                leading=8*mm
            )
        Bold_Style3 = ParagraphStyle(
                "Bold_Style3",
                fontSize=20,
                fontName="Poppins-Bold",
                textColor=colors.HexColor("#612880"),
                alignment=1,
                leading=8*mm
            )
        font_Style1 = ParagraphStyle(
                "font_Style1",
                fontSize=16,
                fontName="Poppins-Regular",
                textColor=colors.black,
                alignment=1,
                leading=8*mm
            )
        font_Style2 = ParagraphStyle(
                "font_Style2",
                fontSize=18,
                fontName="Poppins-Regular",
                textColor=colors.HexColor("#612880"),
                alignment=1,
                leading=8*mm
            )
        #adding text contents of the cover page
        paragraph=[
                    Paragraph(f'{event_name}',Bold_Style1),
                    Spacer(1,14),
                    Paragraph('Industry Inspiration Program',Bold_Style2),
                    Spacer(1,30),
                    Paragraph('Organized by',font_Style1),
                    Spacer(1,240),
                    Paragraph(f'{college_name}',Bold_Style3),
                    Spacer(1,10),
                    Paragraph('In Association with',font_Style1),
                    Spacer(1,125),
                    Paragraph('Seminarroom Education Private Limited',font_Style2)
                ]
        # Create a KeepInFrame to hold the paragraph elements within the frame
        keep_in_frame = KeepInFrame(frame_width, frame_height,paragraph)
        # Build the story within the frame
        frame.addFromList([keep_in_frame], self.canvas)

        #adding images of college logo and seminarroom logo
        #college logo
        college_logo_width,college_logo_height=image_resizer(college_logo,100*mm,75*mm)
        college_logo_x= frame_x + (frame_width - college_logo_width) / 2
        college_logo_y= 120*mm
        self.canvas.drawImage(college_logo, college_logo_x, college_logo_y,college_logo_width,college_logo_height)  

        #semianroom logo
        sr_logo='testing_details/seminarroom logo.png'
        sr_logo_width,sr_logo_height=image_resizer(sr_logo,28*mm,21*mm)
        sr_logo_x= frame_x + (frame_width - sr_logo_width) / 2
        sr_logo_y=53*mm
        self.canvas.drawImage(sr_logo, sr_logo_x, sr_logo_y,sr_logo_width, sr_logo_height)

    ########################################################## PAGE_2 #######################################################
    def add_index(self, index1, index2, index3, index4,index5):
        #adding background and page break
        self.add_background_template()

        #frame
        frame_width = 190*mm # Adjust the width as needed
        frame_height = 180 * mm  # Adjust the height as needed
        frame_x = (page_width - frame_width) / 2 
        frame_y =50* mm
        frame = Frame(frame_x, frame_y, frame_width, frame_height, showBoundary=0)  # Set showBoundary=1 for debugging

        
       
        # Define styles for different parts of the paragraph
        Bold_Style1 = ParagraphStyle(
                "Bold_Style1",
                fontSize=28,
                fontName="Poppins-Bold",
                textColor=colors.HexColor("#612180"),
                alignment=0,
                leading=8*mm
            )
        regular_style= ParagraphStyle(
                "regular_style",
                fontSize=22,
                fontName="Poppins-Regular",
                textColor=colors.HexColor("#612880"),
                alignment=0,
                leading=8*mm
            )
        
        #adding text contents of the cover page
        paragraph=[
                    Paragraph('Content',Bold_Style1),
                    Spacer(1,100),
                    Paragraph(f'01   |    {index1}',regular_style),
                    Spacer(1,40),
                    Paragraph(f'02 |    {index2}',regular_style),
                    Spacer(1,40),
                    Paragraph(f'03 |    {index3}',regular_style),
                    Spacer(1,40),
                    Paragraph(f'04 |    {index4}',regular_style),
                    Spacer(1,40),
                    Paragraph(f'05 |    {index5}',regular_style)
                ]
        # Create a KeepInFrame to hold the paragraph elements within the frame
        keep_in_frame = KeepInFrame(frame_width, frame_height,paragraph)
        # Build the story within the frame
        frame.addFromList([keep_in_frame], self.canvas)

    ########################################################## PAGE_3 #################################################
    def add_about(self,about_p1,about_p2,about_p3,about_p4):
        #adding background and page break
        self.add_background_template()

        #frame
        frame_width = 190*mm # Adjust the width as needed
        frame_height = 215 * mm  # Adjust the height as needed
        frame_x = (page_width - frame_width) / 2 
        frame_y =30* mm
        frame = Frame(frame_x, frame_y, frame_width, frame_height, showBoundary=0)  # Set showBoundary=1 for debugging

        # Define styles for different parts of the paragraph
        Bold_Style1 = ParagraphStyle(
                                        "Bold_Style1",
                                        fontSize=28,
                                        fontName="Poppins-Bold",
                                        textColor=colors.HexColor("#612180"),
                                        alignment=0,
                                        leading=8*mm
                                    )
        font_Style1 = ParagraphStyle(
                                        "font_Style1",
                                        fontSize=16,
                                        fontName="Poppins-Regular",
                                        textColor=colors.black,
                                        alignment=TA_JUSTIFY,
                                        leading=8*mm
                                    )
            
        #adding text contents of the cover page 
        paragraph=[
                        Paragraph(f'About Industry Inspiration Program',Bold_Style1),
                        Spacer(1,40),
                        Paragraph(f'{about_p1}',font_Style1),
                        Spacer(1,10),
                        Paragraph(f'{about_p2}',font_Style1),
                        Spacer(1,10),
                        Paragraph(f'{about_p3}',font_Style1),
                        Spacer(1,10),
                        Paragraph(f'{about_p4}',font_Style1),
                    ]
        
        # Create a KeepInFrame to hold the paragraph elements within the frame
        keep_in_frame = KeepInFrame(frame_width, frame_height,paragraph)
        # Build the story within the frame
        frame.addFromList([keep_in_frame], self.canvas)
    ############################################################# PAGE_4 ###############################################
    def add_about_session(self, topic, date, timings,About_the_Session,learning_outcomes):

        #adding background and page break
        self.add_background_template()

        # Define styles for different parts of the paragraph
        Bold_Style1 = ParagraphStyle(
                                        "Bold_Style1",
                                        fontSize=28,
                                        fontName="Poppins-Bold",
                                        textColor=colors.HexColor("#612180"),
                                        alignment=0,
                                        leading=8*mm
                                    )
        Bold_Style2 = ParagraphStyle(
                                        "Bold_Style2",
                                        fontSize=18,
                                        fontName="Poppins-Bold",
                                        textColor=colors.HexColor("#BA447B"),
                                        alignment=0,
                                        leading=8*mm
                                    )
        Bold_Style5 = ParagraphStyle(
                                        "Bold_Style5",
                                        fontSize=18,
                                        fontName="Poppins-Bold",
                                        textColor=colors.HexColor("#600280"),
                                        alignment=0,
                                        leading=6*mm
                                    )
        font_Style1 = ParagraphStyle(
                                        "font_Style1",
                                        fontSize=16,
                                        fontName="Poppins-Regular",
                                        textColor=colors.black,
                                        alignment=TA_JUSTIFY,
                                        leading=8*mm
                                    )
            
        #adding heading of the page 
        #frame
        frame1_width = 190*mm # Adjust the width as needed
        frame1_height = 230 * mm  # Adjust the height as needed
        frame1_x = (page_width - frame1_width) / 2 
        frame1_y =25* mm
        frame1 = Frame(frame1_x, frame1_y, frame1_width, frame1_height, showBoundary=0)  # Set showBoundary=1 for debugging

        paragraph1=[
                        Paragraph('Industry Inspiration Program',Bold_Style1),
                        Spacer(1,14),
                        Paragraph(f'{topic}',Bold_Style2),
                        Spacer(1,8),
                        Paragraph(f'Date and Time: {date} | {timings}',Bold_Style2),
                        Spacer(1,10),
                        Paragraph('About The Session:',Bold_Style5),
                        Spacer(1,4),
                        Paragraph(f'{About_the_Session}',font_Style1),
                        Spacer(1,6),
                        Paragraph('Learning outcomes:',Bold_Style5),
                        Spacer(1,4),
                        Paragraph(f'{learning_outcomes}',font_Style1),

                    
                    ]
        # Create a KeepInFrame to hold the paragraph elements within the frame
        keep_in_frame1 = KeepInFrame(frame1_width, frame1_height,paragraph1)
        # Build the story within the frame
        frame1.addFromList([keep_in_frame1], self.canvas)
    
    ############################################################# PAGE_5 ###############################################
    def add_about_speaker(self,sme_photo,sme_name,sme_designation,sme_p1, sme_p2, sme_p3):

        #adding background and page break
        self.add_background_template()

        # Define styles for different parts of the paragraph
        Bold_Style1 = ParagraphStyle(
                                        "Bold_Style1",
                                        fontSize=28,
                                        fontName="Poppins-Bold",
                                        textColor=colors.HexColor("#612180"),
                                        alignment=1,
                                        leading=8*mm
                                    )   
        #adding heading of the page 
        #frame
        frame1_width = 190*mm # Adjust the width as needed
        frame1_height = 35 * mm  # Adjust the height as needed
        frame1_x = (page_width - frame1_width) / 2 
        frame1_y =215* mm
        frame1 = Frame(frame1_x, frame1_y, frame1_width, frame1_height, showBoundary=0)  # Set showBoundary=1 for debugging

        paragraph1=[
                        Paragraph('About The Speaker',Bold_Style1)
                    ]
        # Create a KeepInFrame to hold the paragraph elements within the frame
        keep_in_frame1 = KeepInFrame(frame1_width, frame1_height,paragraph1)
        # Build the story within the frame
        frame1.addFromList([keep_in_frame1], self.canvas)

        #adding sme details and timing
        #adding sme description
        #frame
        frame2_width = 120*mm # Adjust the width as needed
        frame2_height = 80 * mm  # Adjust the height as needed
        frame2_x = frame1_x +(frame1_width -frame2_width)
        frame2_y =142* mm
        frame2 = Frame(frame2_x, frame2_y, frame2_width, frame2_height, showBoundary=0)  # Set showBoundary=1 for debugging

        font_Style1 = ParagraphStyle(
                                        "font_Style1",
                                        fontSize=16,
                                        fontName="Poppins-Regular",
                                        textColor=colors.black,
                                        alignment=TA_JUSTIFY,
                                        leading=8*mm
                                    )
        paragraph2=[
                     Paragraph(f'{sme_p1}',font_Style1)
                    ]
        # Create a KeepInFrame to hold the paragraph elements within the frame
        keep_in_frame2 = KeepInFrame(frame2_width, frame2_height,paragraph2)
        # Build the story within the frame
        frame2.addFromList([keep_in_frame2], self.canvas)

        #adding sme photo 76mm,57mm
        # Define the dimensions of the area you want to fill
        sme_photo_width ,sme_photo_height = image_resizer(sme_photo,76*mm,57*mm)
        sme_photo_x=frame1_x+(frame2_x-frame1_x-sme_photo_width) /2
        sme_photo_y=162*mm
        self.canvas.drawImage(sme_photo, sme_photo_x, sme_photo_y, sme_photo_width, sme_photo_height,mask="auto")#set mask ="auto" for background subtracted images

        #frame adding sme name and designation
        frame3_width =frame2_x-frame1_x # Adjust the width as needed
        frame3_height = 20* mm  # Adjust the height as needed
        frame3_x = sme_photo_x + (sme_photo_width- frame3_width)/2
        frame3_y =138* mm
        frame3 = Frame(frame3_x, frame3_y, frame3_width, frame3_height, showBoundary=0)  # Set showBoundary=1 for debugging
        Bold_Style3 = ParagraphStyle(
                                        "Bold_Style3",
                                        fontSize=16,
                                        fontName="Poppins-Bold",
                                        textColor=colors.HexColor("#600280"),
                                        alignment=1,
                                        leading=6*mm
                                    )
        Bold_Style4 = ParagraphStyle(
                                        "Bold_Style3",
                                        fontSize=14,
                                        fontName="Poppins-Bold",
                                        textColor=colors.HexColor("#600280"),
                                        alignment=1,
                                        leading=6*mm
                                    )
        paragraph3=[
                        Paragraph(f'{sme_name}',Bold_Style3),
                        Spacer(1,4),
                        Paragraph(f'{sme_designation}',Bold_Style4),
            
                    ]
        # Create a KeepInFrame to hold the paragraph elements within the frame
        keep_in_frame3 = KeepInFrame(frame3_width, frame3_height,paragraph3)
        # Build the story within the frame
        frame3.addFromList([keep_in_frame3], self.canvas)

        #adding sme para 2 ,3
        frame4_width = 190*mm # Adjust the width as needed
        frame4_height = 117 * mm  # Adjust the height as needed
        frame4_x = (page_width - frame1_width) / 2 
        frame4_y =21* mm
        frame4 = Frame(frame4_x, frame4_y, frame4_width, frame4_height, showBoundary=0)  # Set showBoundary=1 for debugging
        
        paragraph4=[
                        Paragraph(f'{sme_p2}',font_Style1),
                        Spacer(1,8),
                        Paragraph(f'{sme_p3}',font_Style1)
                    ]
        # Create a KeepInFrame to hold the paragraph elements within the frame
        keep_in_frame4 = KeepInFrame(frame4_width, frame4_height,paragraph4)
        # Build the story within the frame
        frame4.addFromList([keep_in_frame4], self.canvas)

    ######################################################## PAGE_6 ########################################################
    def add_feedback_graphs(self, happiness_rating, expectation_rating, knowledge_rating, overall_rating):
        #adding background and page break
        self.add_background_template()
        
        #frame
        frame_width = 190*mm # Adjust the width as needed
        frame_height = 230 * mm  # Adjust the height as needed
        frame_x = (page_width - frame_width) / 2 
        frame_y =25* mm
        frame = Frame(frame_x, frame_y, frame_width, frame_height, showBoundary=0)  # Set showBoundary=1 for debugging

        # Define styles for different parts of the paragraph
        Bold_Style1 = ParagraphStyle(
                                        "Bold_Style1",
                                        fontSize=28,
                                        fontName="Poppins-Bold",
                                        textColor=colors.HexColor("#612180"),
                                        alignment=0,
                                        leading=8*mm
                                    )
        Bold_Style2 = ParagraphStyle(
                                        "Bold_Style2",
                                        fontSize=20,
                                        fontName="Poppins-Bold",
                                        textColor=colors.HexColor("#BA447B"),
                                        alignment=0,
                                        leading=8*mm
                                    )
        font_Style1 = ParagraphStyle(
                                        "font_Style1",
                                        fontSize=16,
                                        fontName="Poppins-Regular",
                                        textColor=colors.black,
                                        alignment=0,
                                        leading=8*mm
                                    )
            
        #adding text contents of the Feedback page 
        paragraph=[
                        Paragraph(f'Feedback',Bold_Style1),
                        Spacer(1,8),
                        Paragraph('Industry Inspiration Program',Bold_Style2),
                        Spacer(1,25),
                        Paragraph("How happy were you with the webinar?",font_Style1),
                        Spacer(1,120),
                        Paragraph("Please rate the speaker's knowledge of the topic",font_Style1),
                        Spacer(1,120),
                        Paragraph("How well did the session meet your expectation?",font_Style1),
                        Spacer(1,120),
                        Paragraph("Please rate your overall experience:",font_Style1),
                    ]
        
        # Create a KeepInFrame to hold the paragraph elements within the frame
        keep_in_frame = KeepInFrame(frame_width, frame_height,paragraph)
        # Build the story within the frame
        frame.addFromList([keep_in_frame], self.canvas)

        #function to genereate bar charts
        def generate_bar_chart(data,x, y ):
            drawing = Drawing(110*mm, 35*mm)

            # Create a VerticalBarChart
            chart = VerticalBarChart()
            chart.width = 110*mm
            chart.height = 32*mm
            chart.x = x
            chart.y = y
            chart.bars.strokeColor = colors.black
            chart.bars.fillColor = colors.aqua
            print("color:",colors.aqua)
            chart.valueAxis.valueMax = 100
            chart.valueAxis.valueStep = 25
            chart.categoryAxis.categoryNames = ['1', '2', '3', '4', '5']
            chart.data = [data]

            # Custom label format function
            def custom_label_format(value):
                return f"{value:.1f}%\n\n"
        
            chart.barLabelFormat = custom_label_format
            drawing.add(chart)
            drawing.wrapOn(self.canvas, 110*mm, 35*mm)
            drawing.drawOn(self.canvas, x, y)

        x=15*mm
        #happiness_rating barchart
        generate_bar_chart(happiness_rating,x,90*mm)
        
        #expectation_rating  barchart
        generate_bar_chart(expectation_rating,x,65*mm)

        # knowledge_rating barchart
        generate_bar_chart( knowledge_rating,x,40*mm)

        #overall_rating barchart
        generate_bar_chart(overall_rating,x,14*mm)
    
    ########################################################## PAGE_7 #####################################################
    def add_feeback(self,fb1,fb2,fb3,fb4,fb5,fb6):
        #adding background and page break
        self.add_background_template()
        
        #frame
        frame_width = 190*mm # Adjust the width as needed
        frame_height = 230 * mm  # Adjust the height as needed
        frame_x = (page_width - frame_width) / 2 
        frame_y =25* mm
        frame = Frame(frame_x, frame_y, frame_width, frame_height, showBoundary=0)  # Set showBoundary=1 for debugging

        # Define styles for different parts of the paragraph
        Bold_Style1 = ParagraphStyle(
                                        "Bold_Style1",
                                        fontSize=24,
                                        fontName="Poppins-Bold",
                                        textColor=colors.HexColor("#612180"),
                                        alignment=0,
                                        leading=8*mm
                                    )
        Bold_Style2 = ParagraphStyle(
                                        "Bold_Style2",
                                        fontSize=20,
                                        fontName="Poppins-Bold",
                                        textColor=colors.HexColor("#BA447B"),
                                        alignment=0,
                                        leading=8*mm
                                    )
        font_Style1 = ParagraphStyle(
                                        "font_Style1",
                                        fontSize=16,
                                        fontName="Poppins-Regular",
                                        textColor=colors.black,
                                        alignment=0,
                                        leading=8*mm
                                    )
        font_Style2 = ParagraphStyle(
                                        "font_Style1",
                                        fontSize=16,
                                        fontName="Poppins-Regular",
                                        textColor=colors.black,
                                        alignment=1,
                                        leading=8*mm
                                    )
        
     
        #adding text contents of the Feedback page 
        paragraph=[
                        Paragraph(f'Feedback',Bold_Style1),
                        Spacer(1,8),
                        Paragraph('Industry Inspiration Program',Bold_Style2),
                        Spacer(1,25),

                        Paragraph(f"{fb1}",font_Style1),
                        Spacer(1,5),
                        Paragraph('____________________________',font_Style2),
                        Spacer(1,5),

                        Paragraph(f"{fb2}",font_Style1),
                        Spacer(1,5),
                        Paragraph('____________________________',font_Style2),
                        Spacer(1,5),

                        Paragraph(f"{fb3}",font_Style1),
                        Spacer(1,5),
                        Paragraph('____________________________',font_Style2),
                        Spacer(1,5)]

        if fb4!="":
            paragraph.extend([
                Paragraph(f"{fb4}", font_Style1),
                Spacer(1, 5),
                Paragraph('____________________________', font_Style2),
                Spacer(1, 5),
            ])

        if fb5!="":
            paragraph.extend([
                Paragraph(f"{fb5}", font_Style1),
                Spacer(1, 5),
                Paragraph('____________________________', font_Style2),
                Spacer(1, 5),
            ])

        if fb6!="":
            paragraph.extend([
                Paragraph(f"{fb6}", font_Style1),
                Spacer(1, 5),
                Paragraph('____________________________', font_Style2),
                Spacer(1, 5),
            ])
        
        # Create a KeepInFrame to hold the paragraph elements within the frame
        keep_in_frame = KeepInFrame(frame_width, frame_height,paragraph)
        # Build the story within the frame
        frame.addFromList([keep_in_frame], self.canvas)

    #################################################### PAGE_8 #################################################################
    def add_snapshots(self,snap1,snap2):
        #adding background and page break
        self.add_background_template()

        #adding heading of the page 
        #frame
        frame1_width = 190*mm # Adjust the width as needed
        frame1_height = 35 * mm  # Adjust the height as needed
        frame1_x = (page_width - frame1_width) / 2 
        frame1_y =215* mm
        frame1 = Frame(frame1_x, frame1_y, frame1_width, frame1_height, showBoundary=0)  # Set showBoundary=1 for debugging

        # Define styles for different parts of the paragraph
        Bold_Style1 = ParagraphStyle(
                                        "Bold_Style1",
                                        fontSize=24,
                                        fontName="Poppins-Bold",
                                        textColor=colors.HexColor("#612180"),
                                        alignment=0,
                                        leading=8*mm
                                    )
        Bold_Style2 = ParagraphStyle(
                                        "Bold_Style2",
                                        fontSize=20,
                                        fontName="Poppins-Bold",
                                        textColor=colors.HexColor("#BA447B"),
                                        alignment=0,
                                        leading=8*mm
                                    )
        paragraph1=[
                        Paragraph(f'Snapshot',Bold_Style1),
                        Spacer(1,8),
                        Paragraph('Industry Inspiration Program',Bold_Style2),
                    ]
        # Create a KeepInFrame to hold the paragraph elements within the frame
        keep_in_frame1 = KeepInFrame(frame1_width, frame1_height,paragraph1)
        # Build the story within the frame
        frame1.addFromList([keep_in_frame1], self.canvas)

        #adding snapshots
        #snap1 
        snap1_width , snap1_height = image_resizer(snap1 ,160*mm,80*mm)
        snap1_x=frame1_x+(frame1_width-snap1_width) /2
        snap1_y=140*mm
        self.canvas.drawImage(snap1, snap1_x, snap1_y, snap1_width, snap1_height)

        #snap2
        snap2_width , snap2_height = image_resizer(snap1,160*mm,80*mm)
        snap2_x=frame1_x+(frame1_width-snap2_width) /2
        snap2_y=50*mm
        self.canvas.drawImage(snap2, snap2_x, snap2_y, snap2_width, snap2_height)

def iip_report_generator(
        event_name, college_name, college_logo, #coverpage 
        index1,index2,index3,index4,index5, #index 
        about_p1,about_p2,about_p3,about_p4, # about page   
        sme_photo,sme_name,sme_designation,sme_p1, sme_p2, sme_p3,# about the speaker
        topic, date, timings,About_the_Session,learning_outcomes, # SME and session  details   
        happiness_rating, expectation_rating, knowledge_rating, overall_rating,#Feedback graph inputs
        fb1,fb2,fb3,fb4,fb5,fb6, #feedback 
        snap1,snap2 #snapshots
        ):

    # Create a temporary folder to store generated certificates
    temp_folder = f'{college_name}_IIP_report'
    os.makedirs(temp_folder, exist_ok=True)

    pdf_canvas = canvas.Canvas(os.path.join(temp_folder, f"{event_name}.pdf"), pagesize=(210*mm,297*mm))
    post = iip_reports(pdf_canvas)
    
    post.add_coverpage(event_name, college_name, college_logo)
   
    post.add_index(index1,index2,index3,index4,index5)

    post.add_about(about_p1,about_p2,about_p3,about_p4)

    post.add_about_session( topic, date, timings,About_the_Session,learning_outcomes)

    post.add_about_speaker(sme_photo, sme_name,sme_designation,sme_p1,sme_p2,sme_p3)

    post.add_feedback_graphs(happiness_rating, expectation_rating, knowledge_rating, overall_rating )

    post.add_feeback(fb1,fb2,fb3,fb4,fb5,fb6)

    post.add_snapshots(snap1,snap2)

    pdf_canvas.save()

    #return pdf_canvas

    # Create a ZIP file containing all certificates
    gen='flask_generated'
    zip_filename = os.path.join(gen, f'{temp_folder}.zip')
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, _, files in os.walk(temp_folder):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, temp_folder))

    return zip_filename

# Delete the temporary directory when you're done with the certificates
def delete_temporary_directory(temp_dir):
    import shutil
    shutil.rmtree(temp_dir, ignore_errors=True)
    
    



