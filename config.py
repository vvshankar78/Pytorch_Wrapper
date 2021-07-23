import pprint

class ModelConfig(object):

	def __init__(self,):
		super(ModelConfig, self).__init__()
		self.seed = 1
		self.batch_size_cuda = 256
		self.batch_size_cpu = 128
		self.num_workers = 4
		# Regularization
		self.dropout = 0
		self.l1_decay = 0
		self.l2_decay = 5e-3
		self.lr = 0.001
		self.momentum = 0.9
		self.epochs = 50
		self.peak = 10
		self.dataset = 'Imagenet' #'Cifar10'
		self.train_data_path = "/tiny-imagenet-200/train"
		self.val_data_path = "/tiny-imagenet-200/val"
		self.train_data_path_engine = "/content/tiny-imagenet-200/train"
		self.val_data_path_engine = "/content/tiny-imagenet-200/val"
		self.url = "http://cs231n.stanford.edu/tiny-imagenet-200.zip"
		self.target_zip = "/tiny-imagenet-200.zip"



	def print_config(self):
		print("Model Parameters:")
		pprint.pprint(vars(self), indent=2)