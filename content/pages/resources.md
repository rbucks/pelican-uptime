Title: Resources
css: resources.css

{% from 'title.html' import title %}
{{ title("Uptime.com Support Resources",
  "Get the web uptime monitoring help and documentation you need.",
  "brand-black",
)}}

{% from 'product.html' import product %}

<div class="container bg-white mb-5">
  <div class="row mb-5">
    {{ product("https://support.uptime.com/hc/en-us",
      "{static}/images/Uptime.com_Support_Help_Desk_Website_Uptime_Monitoring_Software.png",
      "Help Desk",
      "Find FAQs, guides, and chat with 24/7 human support."
    )}}
    {{ product("/api/v1/docs",
      "{static}/images/Uptime.com_API_Documentation_Website_Uptime_Monitoring_Software.png",
      "API Docs",
      "Bring Uptime.com’s functionality into your systems with our API."
    )}}
    {{ product("{filename}quickstart-guide.md",
      "{static}/images/Uptime.com_Quick_Start_Onboarding_Guide_Website_Uptime_Monitoring_Software.png",
      "Quick Start Guide",
      "Get onboarded with Uptime.com's website monitoring platform." 
    )}}
  </div>
</div>

<hr class="mt-5 bg-success"/>

{{ title("Free Web Monitoring Tools",
  "Test your website's domain health, speed, and global uptime.",
  "brand-black",
  2,
)}}

<div class="container bg-white mb-5">
  <div class="row mb-5">
    {{ product("{filename}domain-health.md",
      "{static}/images/Free_Website_Domain_Health_Check_Test_Uptime.com.png",
      "Free Domain Health Test",
      "Monitor your entire domain; web, DNS, email, blacklist and more."
    )}}
    {{ product("/freetools/website-speed-test",
      "{static}/images/Free_Website_Page_Speed_Test_Check_Uptime.com.png",
      "Free Website Speed Test",
      "Enter URLs to check page speed from any global location."
    )}}
    {{ product("/freetools/global-uptime-test",
      "{static}/images/Free_Global_Uptime_Availability_Check_Test_Uptime.com.png",
      "Free Global Uptime Test",
      "Check website response time from locations around the world."
    )}}
  </div>
</div>

<hr class="mt-5 bg-success"/>

{{ title("Uptime.com Published Insights",
  "Test your website's domain health, speed, and global uptime.",
  "Get best practices from fellow users and industry leaders.",
  2,
)}}

<div class="container bg-white mb-5">
  <div class="row mb-5">
    {{ product("/blog",
      "{static}/images/Uptime.com_Blog_Website_Uptime_Performance_Monitoring.png",
      "Blog",
      "Read company and product updates, industry news and more."
    )}}
    {{ product("{filename}success-stories.md",
      "{static}/images/Uptime.com_Case_Studies_Website_Uptime_Performance_Monitoring_Success.png",
      "User Stories",
      "Read the web monitoring stories and wins of users just like you."
    )}}
    <div class="col p-3 m-1"/>
  </div>
</div>
