# Data facts about conversions from Tensorflow 1.x to TensorFlow 2.0

## History

Since the introduction of TensorFlow 2.0 at TensorFlow Dev Summit, it's been already quite some time. Currently, we already see the light at the end of the tunnel. So soon we are going to have a real release of TensorFlow 2.0

Meanwhile, people were able to do some conversion with our service - [tf2up.ml](tf2up.ml).
So I finally decided to take a look at the data, that we have from these conversions.


## How does it work

I decided that just crunching data would be boring, so I decided meanwhile try also Apache Beam + deepen more knowledge and experience with Altair. As a result, I was able to process collected reports of conversion and aggregate them.

Long story short - now we have data in BigQuery, so please approach me if you wanna also analyze it somehow.

From my side, it's just a sneak peek at these conversions.

## Graphs

<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@3"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@4"></script>

<div id="dist_updates"></div>
<div id="top_messages"></div>
<div id="top_not_info"></div>
<div id="ops_dist"></div>

<script src="/static/data/dist_updates.js"></script>
<script src="/static/data/top_messages.js"></script>
<script src="/static/data/top_not_info.js"></script>
<script src="/static/data/ops_dist.js"></script>

<script type="text/javascript">
var opt = {"renderer": "canvas", "actions": false};
vegaEmbed("#dist_updates", dist_updates, opt);
vegaEmbed("#top_messages", top_messages, opt);
vegaEmbed("#top_not_info", top_not_info, opt);
vegaEmbed("#ops_dist", ops_dist, opt);
</script>