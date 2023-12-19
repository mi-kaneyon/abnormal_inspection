import torch
import torchvision.models as models
import torch.nn as nn
from torchvision import transforms
from PIL import Image

# デバイスの設定
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# EfficientNetモデルのロードと内部構造の表示
model = models.efficientnet_v2_s(weights=models.EfficientNet_V2_S_Weights.IMAGENET1K_V1)
print(model)

# 特定の層までのモデルを作成（例：最後の畳み込み層まで）
model_feature_extractor = nn.Sequential(*list(model.children())[:-2])
model_feature_extractor = model_feature_extractor.to(device)

# 特徴量抽出関数
def extract_features(model, image_path, device):
    transform = transforms.Compose([
        transforms.Resize((640, 640)), 
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    # 画像の読み込みと変換
    image = Image.open(image_path)
    image = transform(image).unsqueeze(0).to(device)

    # 特徴量の抽出
    with torch.no_grad():
        features = model(image)
        features = features.view(-1)  # 特徴量ベクトルを平坦化
    return features

# 特徴量抽出のテスト
image_path = 'data/train/sekira/sekira_front-another-copy-_png.rf.e26c06544ff419a6ca0a6dfaf97c4f84.jpg'  # 適切な画像パスに変更してください
features = extract_features(model_feature_extractor, image_path, device)
print("Feature vector shape:", features.shape)  # 特徴量ベクトルの形状を出力

