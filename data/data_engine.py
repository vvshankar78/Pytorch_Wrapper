import torch
import torchvision
import torchvision.transforms as transforms

import pprint

from .data_transforms import albumentations_transforms
from utils import has_cuda, imshow

class DataEngine(object):

	classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog',
			'frog', 'horse', 'ship', 'truck')

	def __init__(self, args):
		super(DataEngine, self).__init__()
		self.batch_size_cuda = args.batch_size_cuda
		self.batch_size_cpu = args.batch_size_cpu
		self.num_workers = args.num_workers
		self.train_data_path = args.train_data_path_engine
		self.test_data_path = args.val_data_path_engine
		self.dataset = args.dataset
		self.load()

	def _transforms(self):
		# Data Transformations
		train_transform = albumentations_transforms(p=1.0, is_train=True)
		test_transform = albumentations_transforms(p=1.0, is_train=False)
		return train_transform, test_transform

	def _dataset(self):
		# Get data transforms
		train_transform, test_transform = self._transforms()
		if self.dataset == 'Cifar10':
		  print('generating datasets for cifar10')
		  train_set = torch.vision.datasets.CIFAR10(root='./../data', train=True, download=True, transform=train_transform)
		  val_set = torchvision.datasets.CIFAR10(root='./../data', train=False, download=True, transform=test_transform)
		elif self.dataset == 'Imagenet':
		  print('generating datasets for Imagenet')
		  train_set = torchvision.datasets.ImageFolder(root=self.train_data_path,transform=train_transform)
		  val_set = torchvision.datasets.ImageFolder(root=self.test_data_path, transform=test_transform)

		return train_set, val_set

	def load(self):
		# Get Train and Test Data
		train_set, val_set = self._dataset()

		# Dataloader Arguments & Test/Train Dataloaders
		dataloader_args = dict(
			shuffle= True,
			batch_size= self.batch_size_cpu)
		if has_cuda():
			dataloader_args.update(
				batch_size= self.batch_size_cuda,
				num_workers= self.num_workers,
				pin_memory= True)

		self.train_loader = torch.utils.data.DataLoader(train_set, **dataloader_args)
		self.val_loader = torch.utils.data.DataLoader(val_set, **dataloader_args)

	def show_samples(self):
		# get some random training images
		dataiter = iter(self.train_loader)
		images, labels = dataiter.next()
		index = []
		num_img = min(len(self.classes), 10)
		for i in range(num_img):
			for j in range(len(labels)):
				if labels[j] == i:
					index.append(j)
					break
		if len(index) < num_img:
			for j in range(len(labels)):
				if len(index) == num_img:
					break
				if j not in index:
					index.append(j)
		imshow(torchvision.utils.make_grid(images[index],
				nrow=num_img, scale_each=True), "Sample train data")

