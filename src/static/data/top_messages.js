var top_messages = {
  "config": {
    "view": {"width": 400, "height": 300},
    "mark": {"tooltip": null},
    "axis": {"labelFontSize": 14, "labelLimit": 450}
  },
  "data": {"name": "data-55da11cf97929d7e4401de1c47960665"},
  "mark": "bar",
  "encoding": {
    "color": {"type": "nominal", "field": "severity"},
    "tooltip": [
      {"type": "quantitative", "field": "seen_times"},
      {"type": "nominal", "field": "message"}
    ],
    "x": {"type": "quantitative", "field": "seen_times"},
    "y": {
      "type": "nominal",
      "field": "message",
      "sort": {"field": "seen_times", "order": "descending"},
      "title": ""
    }
  },
  "title": "Top messages",
  "transform": [
    {
      "window": [{"op": "rank", "field": "seen_times", "as": "rank"}],
      "sort": [{"field": "seen_times", "order": "descending"}]
    },
    {"filter": "(datum.rank < 10)"}
  ],
  "$schema": "https://vega.github.io/schema/vega-lite/v3.4.0.json",
  "datasets": {
    "data-55da11cf97929d7e4401de1c47960665": [
      {
        "message": "Renamed 'tf.contrib.saved_model.load_keras_model' to 'tf.keras.experimental.load_from_saved_model'",
        "severity": "INFO",
        "seen_times": 249
      },
      {
        "message": "Renamed 'tf.global_variables_initializer' to 'tf.compat.v1.global_variables_initializer'",
        "severity": "INFO",
        "seen_times": 171
      },
      {
        "message": "Added keywords to args of function 'tf.boolean_mask'",
        "severity": "INFO",
        "seen_times": 120
      },
      {
        "message": "*.save requires manual check. (This warning is only applicable if the code saves a tf.Keras model) Keras model.save now saves to the Tensorflow SavedModel format by default, instead of HDF5. To continue saving to HDF5, add the argument save_format='h5' to the save() function.",
        "severity": "WARNING",
        "seen_times": 114
      },
      {
        "message": "Changing dataset.make_one_shot_iterator() to tf.compat.v1.data.make_one_shot_iterator(dataset). Please check this transformation.",
        "severity": "WARNING",
        "seen_times": 98
      },
      {
        "message": "Renamed 'tf.app.run' to 'tf.compat.v1.app.run'",
        "severity": "INFO",
        "seen_times": 55
      },
      {
        "message": "Renamed 'tf.zeros_initializer' to 'tf.compat.v1.zeros_initializer'",
        "severity": "INFO",
        "seen_times": 44
      },
      {
        "message": "Renamed 'tf.variable_scope' to 'tf.compat.v1.variable_scope'",
        "severity": "INFO",
        "seen_times": 44
      },
      {
        "message": "Renamed 'tf.placeholder' to 'tf.compat.v1.placeholder'",
        "severity": "INFO",
        "seen_times": 44
      },
      {
        "message": "Changing keep_prob arg of tf.nn.dropout to rate",
        "severity": "INFO",
        "seen_times": 38
      },
      {
        "message": "Renamed 'tf.local_variables_initializer' to 'tf.compat.v1.local_variables_initializer'",
        "severity": "INFO",
        "seen_times": 36
      },
      {
        "message": "Renamed 'tf.random_uniform' to 'tf.random.uniform'",
        "severity": "INFO",
        "seen_times": 32
      },
      {
        "message": "Changing labels arg of tf.nn.softmax_cross_entropy_with_logits to tf.stop_gradient(labels). Please check this transformation.",
        "severity": "INFO",
        "seen_times": 23
      },
      {
        "message": "Changing keep_prob arg of tf.nn.dropout to rate, and recomputing value.",
        "severity": "INFO",
        "seen_times": 22
      },
      {
        "message": "Renamed 'tf.train.StopAtStepHook' to 'tf.estimator.StopAtStepHook'",
        "severity": "INFO",
        "seen_times": 22
      },
      {
        "message": "Renamed 'tf.Session' to 'tf.compat.v1.Session'",
        "severity": "INFO",
        "seen_times": 21
      },
      {
        "message": "tf.estimator.LinearRegressor: Default value of loss_reduction has been changed to SUM_OVER_BATCH_SIZE; inserting old default value tf.compat.v1.losses.Reduction.SUM.",
        "severity": "INFO",
        "seen_times": 20
      },
      {
        "message": "Added keywords to args of function 'tf.argmax'",
        "severity": "INFO",
        "seen_times": 20
      },
      {
        "message": "Changing dataset.make_initializable_iterator() to tf.compat.v1.data.make_initializable_iterator(dataset). Please check this transformation.",
        "severity": "WARNING",
        "seen_times": 18
      },
      {
        "message": "Renamed 'tf.tables_initializer' to 'tf.compat.v1.tables_initializer'",
        "severity": "INFO",
        "seen_times": 16
      },
      {
        "message": "Added keywords to args of function 'tf.reduce_mean'",
        "severity": "INFO",
        "seen_times": 8
      },
      {
        "message": "tf.train.exponential_decay requires manual check. To use learning rate decay schedules with TensorFlow 2.0, switch to the schedules in `tf.keras.optimizers.schedules`.",
        "severity": "INFO",
        "seen_times": 8
      },
      {
        "message": "Changing tf.contrib.layers xavier initializer to a tf.compat.v1.keras.initializers.VarianceScaling and converting arguments.",
        "severity": "INFO",
        "seen_times": 5
      },
      {
        "message": "Renamed 'tf.nn.dynamic_rnn' to 'tf.compat.v1.nn.dynamic_rnn'",
        "severity": "INFO",
        "seen_times": 4
      },
      {
        "message": "Added keywords to args of function 'tf.shape'",
        "severity": "INFO",
        "seen_times": 4
      },
      {
        "message": "Renamed 'tf.losses.sparse_softmax_cross_entropy' to 'tf.compat.v1.losses.sparse_softmax_cross_entropy'",
        "severity": "INFO",
        "seen_times": 4
      },
      {
        "message": "Renamed keyword argument for tf.image.crop_and_resize from box_ind to box_indices",
        "severity": "INFO",
        "seen_times": 3
      },
      {
        "message": "`name` passed to `name_scope`. Because you may be re-entering an existing scope, it is not safe to convert automatically,  the v2 name_scope does not support re-entering scopes by name.",
        "severity": "INFO",
        "seen_times": 3
      },
      {
        "message": "Changing tf.contrib.layers.variance_scaling_initializer to a tf.compat.v1.keras.initializers.VarianceScaling and converting arguments.",
        "severity": "INFO",
        "seen_times": 3
      },
      {
        "message": "Renamed 'tf.data.Iterator' to 'tf.compat.v1.data.Iterator'",
        "severity": "INFO",
        "seen_times": 2
      },
      {
        "message": "Using member tf.contrib.data.sliding_window_batch in deprecated module tf.contrib. tf.contrib.data.sliding_window_batch cannot be converted automatically. tf.contrib will not be distributed with TensorFlow 2.0, please consider an alternative in non-contrib TensorFlow, a community-maintained repository, or fork the required code.",
        "severity": "ERROR",
        "seen_times": 2
      },
      {
        "message": "Renamed 'tf.enable_eager_execution' to 'tf.compat.v1.enable_eager_execution'",
        "severity": "INFO",
        "seen_times": 2
      },
      {
        "message": "Using member tf.contrib.eager.enable_eager_execution in deprecated module tf.contrib. tf.contrib.eager.enable_eager_execution cannot be converted automatically. tf.contrib will not be distributed with TensorFlow 2.0, please consider an alternative in non-contrib TensorFlow, a community-maintained repository, or fork the required code.",
        "severity": "ERROR",
        "seen_times": 2
      },
      {
        "message": "ERROR: Failed to parse.",
        "severity": "ERROR",
        "seen_times": 1
      },
      {
        "message": "Renamed 'tf.get_default_graph' to 'tf.compat.v1.get_default_graph'",
        "severity": "INFO",
        "seen_times": 1
      }
    ]
  }
}