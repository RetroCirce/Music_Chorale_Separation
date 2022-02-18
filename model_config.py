# Configuration of the model training
# Ke Chen
# 2022.02.05

exp_name = "piano_noire_tenor_specunet"
workspace = "/home/kechen/Research/KE_MCS/"
test_output = "wav_output"


dataset_path = "data/"
dataset_name = "piano_noire"
split_file = "idx_string_ni.npy"
sep_track = "tenor"
model_type = "MCS_SpecUNet" # "MCS_ConvTasNet" # "MCS_SpecUNet"

resume_checkpoint = "/home/kechen/Research/KE_MCS/results/piano_noire_bass_tasnet/checkpoint/lightning_logs/version_1/checkpoints/l-epoch=39-mean_sdr=10.285-median_sdr=11.097.ckpt"


loss_type = "mae"   # "si_snr" # "mae"

debug = False

batch_size = 8 * 2
learning_rate = 1e-3
max_epoch = 100
num_workers = 3
lr_scheduler_epoch = [20, 40, 60]
latent_dim = 2048 # deprecated
 
sample_rate = 22050
clip_samples = sample_rate * 10 # audio_set 10-sec clip
segment_frames = 100
hop_samples = 441
random_seed = 12412 # 444612 1536123 12412

# tasnet
tasnet_enc_dim = 512
tasnet_filter_length = 20
tasnet_win = 2
tasnet_feature_dim = 128
tasnet_hidden_dim = 512
tasnet_kernel = 3
tasnet_stack = 3
tasnet_layer = 8
tasnet_causal = False

# recon wave
recon_list = [
    "data/string_ni/h5_file/chorale_001_bass.h5",
    "data/string_ni/h5_file/chorale_001.h5"
]

output_list = [
    "data/recon/chorale_001_bass.wav",
    "data/recon/chorale_001.wav"
]