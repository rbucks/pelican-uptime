title: Website Speed Test Result
<!-- slug: website-speed-test-result
save_as: freetools/website-speed-test/result.html -->
status: draft

{% from 'speed_test_info_box.html' import speed_test_info_box %}
<div class="body-marketing">
	<div id="domain-health-page-header" class="container my-4" style="">
		<h1 class="pt-4" style="">
		<span class="d-block font-16 text-primary" style="">Speed Test Result for</span>
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
	<div id="speed-test-page-results" class="container mb-6">
		<div id="speedTestResultsDisplay">
			<div id="speed-test-header" class="row">
				<div class="col-xl-3 mb-3">
					<img class="mx-auto mb-4 mb-lg-0" style="max-width: 100%;" src="https://uptime.com/media/freetools/screenshots/2022/07/21/www.spider.com_iFKu1VY.png" width="300" height="168">
				</div>
				<div class="col-xl-9">
					<div class="row">
						<div class="col-md-4 mb-3">
							{{ speed_test_info_box('fa-history', 'Loading Time', '2183 ms')}}
						</div>
						<div class="col-md-4 mb-3">
							{{ speed_test_info_box('fa-exchange', 'Requests', '64')}}
						</div>
						<div class="col-md-4 mb-3">
							{{ speed_test_info_box('fa-folder-download', 'Total Size', '1.6 MB')}}
						</div>
						<div class="col-md-4 mb-3">
							{{ speed_test_info_box('fa-tachometer-alt-fast', 'Performance Grade', '85/100')}}
						</div>
						<div class="col-md-4 mb-3">
							{{ speed_test_info_box('fa-mobile-alt', 'Mobile Usability', '100/100')}}
						</div>
						<div class="col-md-4 mb-3">
							<div class="header-block d-block" style="">
								<div class="d-flex align-items-center mb-2" style="">
									<i class="far fa-globe text-primary bg-primary-fade small" style=""></i>
									<span class="value small" style="">Frankfurt, Germany</span>
								</div>
								<div class="d-flex align-items-center" style="">
									<i class="far fa-calendar text-primary bg-primary-fade small" style=""></i>
									<span class="value small" style="">Jul 21, 2022 8:56:09am UTC</span>
								</div>
								</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	{% include 'cta_trial_banner_bottom.html' %}
</div>
