Title: About
css: about.css

{% block description %}
<meta name="description" content="Our passion is peace of mind. Meet the company trusted by thousands of websites to monitor downtime, performance, and domain health with Uptime.com.">
{%endblock%}

<div class="body-container">
  <div class="row-fluid-wrapper">
    <div class="row-fluid">
      <div class="span12 widget-span widget-type-cell" style="" data-widget-type="cell" data-x="0" data-w="12">
        <div class="row-fluid-wrapper row-depth-1 row-number-1 dnd_area-row-0-vertical-alignment bg-success p-5 pb-0 dnd-section dnd_area-row-0-padding">
          <div class="row-fluid ">
            <div class="span12 widget-span widget-type-cell cell_16310722971862-vertical-alignment dnd-column" style="" data-widget-type="cell" data-x="0" data-w="12">
              <div class="row-fluid-wrapper row-depth-1 row-number-2 dnd-row">
                <div class="row-fluid ">
                  <div class="span12 widget-span widget-type-custom_widget widget_1631072296680-hidden dnd-module" style="" data-widget-type="custom_widget" data-x="0" data-w="12">
                    <div id="hs_cos_wrapper_widget_1631072296680" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">
                      <div id="" class="atmc-image-default flex justify-center fadeInBottom ">
                        <div class="text-center">
                          <img loading="lazy" src="/images/Learn_More_Uptime.com_Website_Uptime_Performance_Monitoring_Services.webp" alt="Learn More Uptime.com for Website Uptime Performance Monitoring Services" width="100%" style="max-width: 730px; max-height: 260px">
                        </div>
                      </div>
                    </div>
                  </div>
                  <!--end widget-span -->
                </div>
                <!--end row-->
              </div>
              <!--end row-wrapper -->
            </div>
            <!--end widget-span -->
          </div>
          <!--end row-->
        </div>
        {% from 'banner.html' import banner %} 
        {{ banner("<span>Learn about <span class='text-success'>Uptime.com</span></span>",
          "Our passion is peace of mind. Meet the company trusted to monitor the world's top websites.",
          "",
          "bg-success",
        )}}
        {% from 'image_block.html' import image_block %}
        {{ image_block("left", "/images/Founding_Team_for_Uptime.com_Website_Uptime_Performance_Monitoring_Platform.webp",
        "",
        "Monitoring since 2013",
        "<span>Uptime.com was founded after we experienced a major web outage and couldn’t find a solution that was both affordable and user-friendly.</span><br><span>Turns out we weren’t alone.</span>",
        "bg-success") 
        }}
        {{ image_block("left", "/images/Best_Website_Uptime_Monitoring_Services_with_Uptime.com_890x750.webp",
        "",
        "Thousands of customers later...",
        "Our unique combination of top-rated website monitoring technology and 100% dedicated human support has gotten us recognized as one of the world's best solutions to use (and work with) for nearly a decade.",
        "bg-success") 
        }} 
        {{ banner("Our core values are a superpower",
          "See the values Uptime.com was built on.",
          "",
          "d-none",
        )}}
          {% from 'icon_text.html' import icon_text %}
          <div class="row no-gutters bg-light-gray">
            <div class="col-6">
            {{ icon_text(
              "/images/Customer_First_Approach_Website_Uptime_Performance_Monitoring.svg",
              "Customer-first",
              "User experience is at the forefront of every design decision Uptime.com makes. Our streamlined setup makes it easy to create checks and alerts. Dashboards instantly display important stats and allow you to dig deeper into checks. Don’t want to log into your account to check the status everyday? Integrate with your favorite DevOps tools like Slack, PagerDuty, and more.",
              ) }}
            </div>
            <div class="col-6">
            {{ icon_text(
              "/images/Comprehensive_Approach_Website_Uptime_Performance_Downtime_Monitoring.svg",
              "Comprehensive",
              "Uptime.com does more than check site availability. Monitor for other critical site problems and performance issues. Download reports to share with management or other team members. We provide you with crucial details for accurate root cause analysis. Create public-facing status pages and widgets to share information with site visitors.",
              ) }}
            </div>
            <div class="col-6">
            {{ icon_text(
              "/images/Immediate_Technical_Customer_Support_Website_Uptime_Performance_Monitoring.svg",
              "Supportive",
              "Don't wait days for an answer when you need resolution in minutes. Our support library provides detailed answers to pressing questions. Need more? We’re always available via live chat, email, phone, or contact form. You’ll get immediate personal attention from a technical support expert.",
              ) }}
            </div>
            <div class="col-6">
            {{ icon_text(
              "/images/Reliable_Website_Uptime_Monitoring_Less_False_Downtime_Outage_Alerts.svg",
              "Reliable",
              "When it comes to web monitoring, reliability is everything. That’s why we’ve worked tirelessly to create a highly reliable system that mitigates false alarms. This means you can continuously (and confidently) monitor website performance with little to no false positives and total peace of mind.",
              ) }}
            </div>
          </div>
          <div class="bg-light-gray pb-4">
            <hr class="mt-0 mb-0 bg-success">
          </div>
        {% from 'testimonial.html' import testimonial %}
        {{ testimonial("/images/User_Review_Uptime.com_Website_Performance_Monitoring_Downtime_Outage_Checks.webp",
          "bg-success",
          "Interesting work with amazing people",
          "The collaboration is incredible. Everyone is smart and engaged, sharing ideas and looking for improvement. And getting feedback from customers who love what we do for them makes it all very satisfying. The fully-remote work really suits my lifestyle, and company-wide meetups are always a lot of fun as well.")}}
      </div>
      <!--end widget-span -->
    </div>
  </div>
</div>
