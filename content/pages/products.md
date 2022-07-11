Title: Products

{% from 'banner.html' import banner %} 
{{ banner("Uptime Monitoring Products",
  "Explore our top-rated website performance monitoring tools.",
  "bg-white",
  "bg-success"
)}}

{% from 'product.html' import product %} 
<div class="container bg-white mb-5">
  <div class="row mb-5">
    {{ product("{filename}monitoring.md",
      "{static}/images/Website_Uptime_Monitoring_Checks_with_Uptime.com.png",
      "Uptime Monitoring",
      "Web monitoring checks for HTTP(S), SSL, synthetics and more."
    )}}

    {{ product("{filename}alerting.md",
      "{static}/images/IT_Alert_Notifications_for_Website_Outages_with_Uptime.com.png",
      "Alerting",
      "Web downtime and incident alerts via SMS/call, email, and more."
    )}}

    {{ product("{filename}reporting.md",
      "{static}/images/Website_Performance_Monitoring_Reporting_and_Analytics_with_Uptime.com.png",
      "Reporting",
      "Custom dashboards and scheduled uptime performance reports."
    )}}  
  </div>
  <div class="row mb-5">
    {{ product("{filename}real-user-monitoring.md",
      "{static}/images/Real_User_Monitoring_(RUM)_page_speed_errors_Uptime.com.png",
      "RUM",
      "Real User Monitoring for page speed, errors, and site experience."
    )}}

    {{ product("{filename}status-pages.md",
      "{static}/images/Custom_Website_Status_Pages_Uptime.com.png",
      "Status Pages",
      "Customizable status pages for internal and external use."
    )}}

    {{ product("{filename}integrations.md",
      "{static}/images/Website_Uptime_Performance_Monitoring_Integrations_Uptime.com.png",
      "Integrations",
      "Integrate with dozens of DevOps tools like Slack and PagerDuty."
    )}}  
  </div>
</div>


{{ banner("Uptime Monitoring For Industries",
  "Learn how Uptime.com helps various industries with website performance.",
  "bg-white",
  "bg-success"
)}}


<div class="container bg-white mb-5">
  <div class="row mb-5">
    {{ product("{filename}ecommerce-websites-uptime.md",
      "{static}/images/Ecommerce_Businesses_Trust_Uptime.com_Monitoring.png",
      "Ecommerce Website Monitoring",
      "Used by online sellers to test site reliability, speed, and transactions."
    )}}

    {{ product("{filename}edu-websites-uptime.md",
      "{static}/images/Education_And_Universities_trust_Uptime.com_Monitoring.png",
      "Education Website Monitoring",
      "Used by .edu websites monitor downtime and user experience."
    )}}

    {{ product("{filename}financial-websites-uptime.md",
      "{static}/images/Financial_Industries_Trust_Uptime.com_Monitoring.png",
      "Financial Services Website Monitoring",
      "Trusted to securely check website speed, errors, and performance."
    )}}  
  </div>
  <div class="row mb-5">
    {{ product("{filename}it-services-uptime.md",
      "{static}/images/IT_Services_Trusts_Uptime.com_Monitoring.png",
      "IT Pro Services Monitoring",
      "Trusted by leading IT companies to monitor infrastructure uptime."
    )}}

    {{ product("{filename}saas-websites-uptime.md",
      "{static}/images/Software_SAAS_B2B_Industries_Trust_Uptime.com_Monitoring.png",
      "SaaS Website Monitoring",
      "Trusted by SaaS brands to monitor website speed and performance."
    )}} 

     <div class="col p-3 m-1">
     </div> 
  </div>
</div>