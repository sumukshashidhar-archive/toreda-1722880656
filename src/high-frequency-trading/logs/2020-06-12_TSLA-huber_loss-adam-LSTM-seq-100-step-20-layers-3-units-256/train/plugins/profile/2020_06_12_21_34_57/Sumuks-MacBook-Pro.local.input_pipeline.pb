	\���(J@\���(J@!\���(J@	��d{�?��d{�?!��d{�?"g
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails&\���(J@`��"��G@A}?5^�I@Y��C�l�?*	     8�@2F
Iterator::Model�V-�?!D��GPQW@)L7�A`��?1G�2���U@:Preprocessing2S
Iterator::Model::ParallelMap{�G�z�?!��x7Ɉ@){�G�z�?1��x7Ɉ@:Preprocessing2j
3Iterator::Model::ParallelMap::Zip[1]::ForeverRepeaty�&1��?!�܀�%@)���S㥛?1���B@:Preprocessing2t
=Iterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate��~j�t�?!j}L�%u@)�~j�t��?1^�*�W��?:Preprocessing2�
MIterator::Model::ParallelMap::Zip[0]::FlatMap[0]::Concatenate[0]::TensorSlicey�&1�|?!�܀�%�?)y�&1�|?1�܀�%�?:Preprocessing2d
-Iterator::Model::ParallelMap::Zip[0]::FlatMap�I+��?!��щ�@)�~j�t�h?1^�*�W��?:Preprocessing2v
?Iterator::Model::ParallelMap::Zip[1]::ForeverRepeat::FromTensor����MbP?!?&ǒ::�?)����MbP?1?&ǒ::�?:Preprocessing:�
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
�Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
�Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
�Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
�Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)�
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis�
device�Your program is NOT input-bound because only 1.4% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*high2B91.6 % of the total step time sampled is spent on All Others time.#You may skip the rest of this page.B�
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown�
	`��"��G@`��"��G@!`��"��G@      ��!       "      ��!       *      ��!       2	}?5^�I@}?5^�I@!}?5^�I@:      ��!       B      ��!       J	��C�l�?��C�l�?!��C�l�?R      ��!       Z	��C�l�?��C�l�?!��C�l�?JCPU_ONLY