title: Domain Health Check
slug: domain-health-check
save_as: domain-health/check.html
{% from 'check_summary_box.html' import check_summary_box %}
{% from 'check_results_table.html' import check_results_table %}
<div class="body-marketing">
	<div id="domain-health-page-header" class="container my-4" style="">
		<h1 class="pt-4" style="">
		<span class="d-block font-16 text-primary" style="">Domain Health Check for</span>
		<span class="d-block font-32 " style="">
			www.spider.com
			<a
				target="_blank"
				class="font-18 text-primary"
				href="http://www.spider.com" style="">
				<i class="fas fa-external-link-alt" style="vertical-align: 3px;"></i>
			</a>
		</span>
		</h1>
	</div>
	<div id="domain-health-page-results" class="container mb-6">
		<div class="row mb-5">
			<div class="col-sm-6 col-lg-3 mb-3 mb-lg-0">
				{{ check_summary_box('DNS', 'fa-sliders-h' , 3, 2, 1)}}
			</div>
			<div class="col-sm-6 col-lg-3 mb-3 mb-lg-0">
				{{ check_summary_box('Web Server', 'fa-globe' , 3, 2, 1)}}
			</div>
			<div class="col-sm-6 col-lg-3 mb-3 mb-lg-0">
				{{ check_summary_box('Mail Server', 'fa-envelope' , 3, 2, 1)}}
			</div>
			<div class="col-sm-6 col-lg-3 mb-3 mb-lg-0">
				{{ check_summary_box('Blacklist/Malware', 'fa-bug fa-lg' , 3, 2, 1)}}
			</div>
		</div>
		<div class="create-checks-bar bg-primary sticky-top mb-5">
			<div class="d-md-flex align-items-md-center">
				<div class="mb-3 mb-md-0" style="flex: 1 1 50%;">
					<h4 class="text-white">Checks Selected: 7</h4>
					<p class="mb-0">Select<span></span>
					<a class="text-white" href="#">all</a>,
					<span> </span>
					<a class="text-white" href="#">none</a><span> </span>or individually below.</p>
				</div>
				<div style="flex: 1 1 50%;">
					<div class="d-md-flex align-items-md-center">
						<p class="mb-3 mb-md-0 mr-4">Start a 21-day free trial (no credit card required) to schedule these checks.</p>
						<button class="btn btn-white text-primary">Start Free Trial</button>
					</div>
				</div>
			</div>
		</div>
		<div class="mb-5">
			{{ check_results_table('DNS', 'fa-sliders-h', [])}}
		</div>
		<div class="mb-5">
			{{ check_results_table('Web Server', 'fa-globe', [])}}
		</div>
		<div class="mb-5">
			{{ check_results_table('Blacklist/Malware', 'fa-bug', [])}}
		</div>
	</div>
</div>
{% include 'cta_trial_banner_bottom.html' %}
</div>