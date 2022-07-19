Title: Success Stories

<div class="container bg-white my-5">
  <h1 class="mt-4 text-center">Uptime means customer success</h1>
  <p class="mb-4 text-center subheading">Hear stories from website monitoring users just like you.</p>

  {% from 'product.html' import product %} 
  <div class="row mb-5">
    {{ product("{filename}guild-education.md",
      "{static}/images/Customer_Success_Guild.png",
      "Guild",
      "Improving visibility into web app performance and experience"
    )}}

    {{ product("{filename}condeco.md",
      "{static}/images/Customer_Success_Condeco.png",
      "Condeco",
      "Helping provide the best possible website user experience"
    )}}

    {{ product("{filename}newswire.md",
      "{static}/images/Customer_Success_Newswire.png",
      "Newswire",
      "Partnering to deliver website performance and reliability"
    )}}
  </div>
  <div class="row mb-5">
    {{ product("{filename}800.md",
      "{static}/images/Customer_Success_800.com.png",
      "800.com",
      "Improving observability with web performance monitoring "
    )}}

    {{ product("{filename}epurple.md",
      "{static}/images/Customer_Success_Epurple.png",
      "Epurple",
      "Reliably monitoring and reporting on website performance"
    )}}

    {{ product("{filename}transcepta.md",
      "{static}/images/Customer_Success_Transcepta.png",
      "Transcepta",
      "Resolving incidents before customers are impacted"
    )}}
  </div>
  <div class="row mb-5">
    {{ product("{filename}socketlabs.md",
      "{static}/images/SocketLabs_Trusts_Uptime.com_CaseStudy.png",
      "SocketLabs",
      "Offering accurate and reliable external uptime monitoring "
    )}}

    <div class="col"></div>
    <div class="col"></div>
  </div>
</div> 


{% from 'banner.html' import banner %} 
{{ banner("Helping <span class='text-success'>thousands</span> of customers",
  "check website uptime, page speed, user experience, and domain health.",
  "bg-light-gray",
  "bg-success"
)}}


{% from 'image_block.html' import image_block %}
{{ image_block("left", "{static}/images/Web_Monitoring_Customer_Support.png",
"UPTIME MONITORING SUPPORT",
"Count on top-rated support resources",
"Products alone don't solve problems, people do. Ask any question, search popular topics, access FAQ guides -- and get support help when you need it.") }}

{{ image_block("right", "{static}/images/Award_Winning_Web_Monitoring_Tools.png",
"UPTIME MONITORING SUCCESS",
"Recognized for customer success",
"By thousands of customers who love the responsiveness and reliability of our award-winning customer success and support team.
<br/><br/>
By analysts like G2 & TechRadar who rate us one of the world’s easiest website uptime monitoring services to work with.") }}


{% from 'testimonial.html' import testimonial %}
{{ testimonial("{static}/images/Review_Victor.png",
  "bg-success",
  "Amazing!",
  "NRC was looking for a monitoring tool to replace the one we currently had. We used PINGDOM, DataDog, PRTG, and other services during our initial review. We ended up choosing uptime! Their customer service was very polite and fast. Their interface was very easy and user friendly. Their knowledge base articles also helped out a lot as we had questions. Most of all they give you the proper bang for your buck!")}}


{% from 'cta_bottom.html' import cta_bottom %} 
{{ cta_bottom("Customer success runs on website uptime",
  ("100% human live chat", 
  "In-app on screen assistance",
  "Global support across time zones",
  "Direct escalation to uptime devs")
  )}}