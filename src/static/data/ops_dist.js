var ops_dist = {
  "config": {
    "view": {"width": 400, "height": 300},
    "mark": {"tooltip": null},
    "axis": {"labelLimit": 800, "titleFontSize": 14}
  },
  "data": {"name": "data-cab2ab22bd5bcf41360d827e4a443d3c"},
  "mark": {"type": "circle", "size": 60},
  "encoding": {
    "color": {"type": "nominal", "field": "severity"},
    "tooltip": [
      {"type": "nominal", "field": "op"},
      {"type": "nominal", "field": "message"},
      {"type": "quantitative", "field": "seen_times"},
      {"type": "quantitative", "field": "seen_files"}
    ],
    "x": {"type": "quantitative", "field": "seen_times"},
    "y": {"type": "quantitative", "field": "seen_files"}
  },
  "title": "Ops seen in conversions",
  "$schema": "https://vega.github.io/schema/vega-lite/v3.4.0.json",
  "datasets": {
    "data-cab2ab22bd5bcf41360d827e4a443d3c": [
      {
        "op": "tf.compat.v1.global_variables_initializer",
        "severity": "INFO",
        "seen_times": 154,
        "seen_files": 2,
        "message": "Renamed 'tf.global_variables_initializer' to 'tf.compat.v1.global_variables_initializer'"
      },
      {
        "op": "tf.keras.experimental.load_from_saved_model",
        "severity": "INFO",
        "seen_times": 144,
        "seen_files": 1,
        "message": "Renamed 'tf.contrib.saved_model.load_keras_model' to 'tf.keras.experimental.load_from_saved_model'"
      },
      {
        "op": "tf.boolean_mask",
        "severity": "INFO",
        "seen_times": 120,
        "seen_files": 1,
        "message": "Added keywords to args of function 'tf.boolean_mask'"
      },
      {
        "op": "tf.Keras",
        "severity": "WARNING",
        "seen_times": 116,
        "seen_files": 5,
        "message": "*.save requires manual check. (This warning is only applicable if the code saves a tf.Keras model) Keras model.save now saves to the Tensorflow SavedModel format by default, instead of HDF5. To continue saving to HDF5, add the argument save_format='h5' to the save() function."
      },
      {
        "op": "tf.contrib.saved_model.load_keras_model",
        "severity": "INFO",
        "seen_times": 105,
        "seen_files": 1,
        "message": "Renamed 'tf.contrib.saved_model.load_keras_model' to 'tf.keras.experimental.load_from_saved_model'"
      },
      {
        "op": "tf.compat.v1.data.make_one_shot_iterator",
        "severity": "WARNING",
        "seen_times": 98,
        "seen_files": 13,
        "message": "Changing dataset.make_one_shot_iterator() to tf.compat.v1.data.make_one_shot_iterator(dataset). Please check this transformation."
      },
      {
        "op": "tf.nn.dropout",
        "severity": "INFO",
        "seen_times": 60,
        "seen_files": 3,
        "message": "Changing keep_prob arg of tf.nn.dropout to rate"
      },
      {
        "op": "tf.compat.v1.app.run",
        "severity": "INFO",
        "seen_times": 55,
        "seen_files": 1,
        "message": "Renamed 'tf.app.run' to 'tf.compat.v1.app.run'"
      },
      {
        "op": "tf.placeholder",
        "severity": "INFO",
        "seen_times": 44,
        "seen_files": 2,
        "message": "Renamed 'tf.placeholder' to 'tf.compat.v1.placeholder'"
      },
      {
        "op": "tf.compat.v1.local_variables_initializer",
        "severity": "INFO",
        "seen_times": 36,
        "seen_files": 2,
        "message": "Renamed 'tf.local_variables_initializer' to 'tf.compat.v1.local_variables_initializer'"
      },
      {
        "op": "tf.zeros_initializer",
        "severity": "INFO",
        "seen_times": 22,
        "seen_files": 1,
        "message": "Renamed 'tf.zeros_initializer' to 'tf.compat.v1.zeros_initializer'"
      },
      {
        "op": "tf.compat.v1.variable_scope",
        "severity": "INFO",
        "seen_times": 22,
        "seen_files": 1,
        "message": "Renamed 'tf.variable_scope' to 'tf.compat.v1.variable_scope'"
      },
      {
        "op": "tf.compat.v1.zeros_initializer",
        "severity": "INFO",
        "seen_times": 22,
        "seen_files": 1,
        "message": "Renamed 'tf.zeros_initializer' to 'tf.compat.v1.zeros_initializer'"
      },
      {
        "op": "tf.variable_scope",
        "severity": "INFO",
        "seen_times": 22,
        "seen_files": 1,
        "message": "Renamed 'tf.variable_scope' to 'tf.compat.v1.variable_scope'"
      },
      {
        "op": "tf.Session",
        "severity": "INFO",
        "seen_times": 21,
        "seen_files": 2,
        "message": "Renamed 'tf.Session' to 'tf.compat.v1.Session'"
      },
      {
        "op": "tf.compat.v1.losses.Reduction.SUM.",
        "severity": "INFO",
        "seen_times": 20,
        "seen_files": 2,
        "message": "tf.estimator.LinearRegressor: Default value of loss_reduction has been changed to SUM_OVER_BATCH_SIZE; inserting old default value tf.compat.v1.losses.Reduction.SUM."
      },
      {
        "op": "tf.argmax",
        "severity": "INFO",
        "seen_times": 20,
        "seen_files": 1,
        "message": "Added keywords to args of function 'tf.argmax'"
      },
      {
        "op": "tf.compat.v1.data.make_initializable_iterator",
        "severity": "WARNING",
        "seen_times": 18,
        "seen_files": 1,
        "message": "Changing dataset.make_initializable_iterator() to tf.compat.v1.data.make_initializable_iterator(dataset). Please check this transformation."
      },
      {
        "op": "tf.global_variables_initializer",
        "severity": "INFO",
        "seen_times": 17,
        "seen_files": 1,
        "message": "Renamed 'tf.global_variables_initializer' to 'tf.compat.v1.global_variables_initializer'"
      },
      {
        "op": "tf.random.uniform",
        "severity": "INFO",
        "seen_times": 16,
        "seen_files": 1,
        "message": "Renamed 'tf.random_uniform' to 'tf.random.uniform'"
      },
      {
        "op": "tf.random_uniform",
        "severity": "INFO",
        "seen_times": 16,
        "seen_files": 1,
        "message": "Renamed 'tf.random_uniform' to 'tf.random.uniform'"
      },
      {
        "op": "tf.stop_gradient",
        "severity": "INFO",
        "seen_times": 13,
        "seen_files": 2,
        "message": "Changing labels arg of tf.nn.softmax_cross_entropy_with_logits to tf.stop_gradient(labels). Please check this transformation."
      },
      {
        "op": "tf.train.StopAtStepHook",
        "severity": "INFO",
        "seen_times": 11,
        "seen_files": 1,
        "message": "Renamed 'tf.train.StopAtStepHook' to 'tf.estimator.StopAtStepHook'"
      },
      {
        "op": "tf.estimator.StopAtStepHook",
        "severity": "INFO",
        "seen_times": 11,
        "seen_files": 1,
        "message": "Renamed 'tf.train.StopAtStepHook' to 'tf.estimator.StopAtStepHook'"
      },
      {
        "op": "tf.nn.softmax_cross_entropy_with_logits",
        "severity": "INFO",
        "seen_times": 10,
        "seen_files": 1,
        "message": "Changing labels arg of tf.nn.softmax_cross_entropy_with_logits to tf.stop_gradient(labels). Please check this transformation."
      },
      {
        "op": "tf.reduce_mean",
        "severity": "INFO",
        "seen_times": 8,
        "seen_files": 1,
        "message": "Added keywords to args of function 'tf.reduce_mean'"
      },
      {
        "op": "tf.compat.v1.tables_initializer",
        "severity": "INFO",
        "seen_times": 8,
        "seen_files": 1,
        "message": "Renamed 'tf.tables_initializer' to 'tf.compat.v1.tables_initializer'"
      },
      {
        "op": "tf.tables_initializer",
        "severity": "INFO",
        "seen_times": 8,
        "seen_files": 1,
        "message": "Renamed 'tf.tables_initializer' to 'tf.compat.v1.tables_initializer'"
      },
      {
        "op": "tf.train.exponential_decay",
        "severity": "INFO",
        "seen_times": 8,
        "seen_files": 1,
        "message": "tf.train.exponential_decay requires manual check. To use learning rate decay schedules with TensorFlow 2.0, switch to the schedules in `tf.keras.optimizers.schedules`."
      },
      {
        "op": "tf.contrib.layers",
        "severity": "INFO",
        "seen_times": 5,
        "seen_files": 1,
        "message": "Changing tf.contrib.layers xavier initializer to a tf.compat.v1.keras.initializers.VarianceScaling and converting arguments."
      },
      {
        "op": "tf.nn.dynamic_rnn",
        "severity": "INFO",
        "seen_times": 4,
        "seen_files": 1,
        "message": "Renamed 'tf.nn.dynamic_rnn' to 'tf.compat.v1.nn.dynamic_rnn'"
      },
      {
        "op": "tf.shape",
        "severity": "INFO",
        "seen_times": 4,
        "seen_files": 1,
        "message": "Added keywords to args of function 'tf.shape'"
      },
      {
        "op": "tf.compat.v1.losses.sparse_softmax_cross_entropy",
        "severity": "INFO",
        "seen_times": 4,
        "seen_files": 1,
        "message": "Renamed 'tf.losses.sparse_softmax_cross_entropy' to 'tf.compat.v1.losses.sparse_softmax_cross_entropy'"
      },
      {
        "op": "tf.contrib.layers.variance_scaling_initializer",
        "severity": "INFO",
        "seen_times": 3,
        "seen_files": 1,
        "message": "Changing tf.contrib.layers.variance_scaling_initializer to a tf.compat.v1.keras.initializers.VarianceScaling and converting arguments."
      },
      {
        "op": "tf.image.crop_and_resize",
        "severity": "INFO",
        "seen_times": 3,
        "seen_files": 1,
        "message": "Renamed keyword argument for tf.image.crop_and_resize from box_ind to box_indices"
      },
      {
        "op": "tf.contrib.data.sliding_window_batch",
        "severity": "ERROR",
        "seen_times": 2,
        "seen_files": 1,
        "message": "Using member tf.contrib.data.sliding_window_batch in deprecated module tf.contrib. tf.contrib.data.sliding_window_batch cannot be converted automatically. tf.contrib will not be distributed with TensorFlow 2.0, please consider an alternative in non-contrib TensorFlow, a community-maintained repository, or fork the required code."
      },
      {
        "op": "tf.compat.v1.get_default_graph",
        "severity": "INFO",
        "seen_times": 1,
        "seen_files": 1,
        "message": "Renamed 'tf.get_default_graph' to 'tf.compat.v1.get_default_graph'"
      },
      {
        "op": "tf.data.Iterator",
        "severity": "INFO",
        "seen_times": 1,
        "seen_files": 1,
        "message": "Renamed 'tf.data.Iterator' to 'tf.compat.v1.data.Iterator'"
      },
      {
        "op": "tf.compat.v1.data.Iterator",
        "severity": "INFO",
        "seen_times": 1,
        "seen_files": 1,
        "message": "Renamed 'tf.data.Iterator' to 'tf.compat.v1.data.Iterator'"
      },
      {
        "op": "tf.compat.v1.enable_eager_execution",
        "severity": "INFO",
        "seen_times": 1,
        "seen_files": 1,
        "message": "Renamed 'tf.enable_eager_execution' to 'tf.compat.v1.enable_eager_execution'"
      },
      {
        "op": "tf.enable_eager_execution",
        "severity": "INFO",
        "seen_times": 1,
        "seen_files": 1,
        "message": "Renamed 'tf.enable_eager_execution' to 'tf.compat.v1.enable_eager_execution'"
      },
      {
        "op": "tf.contrib.eager.enable_eager_execution",
        "severity": "ERROR",
        "seen_times": 1,
        "seen_files": 1,
        "message": "Using member tf.contrib.eager.enable_eager_execution in deprecated module tf.contrib. tf.contrib.eager.enable_eager_execution cannot be converted automatically. tf.contrib will not be distributed with TensorFlow 2.0, please consider an alternative in non-contrib TensorFlow, a community-maintained repository, or fork the required code."
      },
      {
        "op": "tf.contrib.",
        "severity": "ERROR",
        "seen_times": 1,
        "seen_files": 1,
        "message": "Using member tf.contrib.eager.enable_eager_execution in deprecated module tf.contrib. tf.contrib.eager.enable_eager_execution cannot be converted automatically. tf.contrib will not be distributed with TensorFlow 2.0, please consider an alternative in non-contrib TensorFlow, a community-maintained repository, or fork the required code."
      }
    ]
  }
}