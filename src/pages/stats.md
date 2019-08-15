# Data facts about conversions from Tensorflow 1.x to TensorFlow 2.0

## History

Since the introduction of TensorFlow 2.0 at TensorFlow Dev Summit, it's been already quite some time. Currently, we already see the light at the end of the tunnel. So soon we are going to have a real release of TensorFlow 2.0

Meanwhile, people were able to do some conversion with our service - [tf2up.ml](tf2up.ml).
So I finally decided to take a look at the data, that we have from these conversions.


## How does it work

I decided that just crunching data would be boring, so I decided meanwhile try also Apache Beam[^Beam] + deepen more knowledge and experience with Altair[^Altair]. As a result, I was able to process collected conversion reports and aggregate them.

Long story short - now we have data in BigQuery, so please approach me if you wanna also analyze it somehow.

From my side, it's just a sneak peek at these conversions.

## Graphs
Here are a couple of graphs in Altair. So feel free to hower, to see more details.

<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@3"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@4"></script>

<div id="dist_updates" class="cntr"></div>
First question: how many changes per file we need?
Looks like, from my sample, the median is around 8 changes per file.


<div id="top_messages"></div>

What are the most common messages we see during conversion?
No big surpsises here:

- many people need to load models from Keras saved model

> `tf.contrib.saved_model.load_keras_model` -> `tf.keras.experimental.load_from_saved_model`

- `tf.global_variables_initializer` is going to leave us for better :)

<div id="top_not_info"></div>

What are the top messages, that not just info:
- Keras `model.save` now saves to the Tensorflow SavedModel format by default.
- `dataset.make_one_shot_iterator()` datasets in 2.0 are also eager and simpler to iterrate, but that means that in old lagecy places we would need to replace them. There is an updated section on TensorFlow tutorial section for 2.0[^dataset2]

<div id="ops_dist" class="cntr"></div>

And from the number of files, dataset would affect the most, since everyone, needs to feed data.

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

[^Altair]: [Altair: Declarative Visualization in Python](https://altair-viz.github.io/)
[^Beam]: [Apache Beam](https://beam.apache.org/)
[^dataset2]: [Load images with tf.data](https://www.tensorflow.org/beta/tutorials/load_data/images)