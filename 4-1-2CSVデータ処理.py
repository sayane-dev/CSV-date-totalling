import csv
from collections import defaultdict

# CSVファイルのパス（複数対応）
csv_files = [
    '/Users/sayane/Desktop/課題2.csv',
    '/Users/sayane/Desktop/課題3.csv'
]

# 各参加者のスコアを格納する辞書
scores_by_person = defaultdict(list)

# 複数のCSVファイルを読み込む
for csv_file in csv_files:
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # 空行をスキップ
                if not row.get('名前') or not row.get('スコア'):
                    continue
                name = row['名前']
                score = int(row['スコア'])
                scores_by_person[name].append(score)
        print(f"✓ {csv_file} を読み込みました")
    except FileNotFoundError:
        print(f"⚠ 警告: {csv_file} が見つかりませんでした")
    except Exception as e:
        print(f"⚠ エラー: {csv_file} の読み込み中にエラーが発生しました: {e}")

# 各参加者の統計情報を計算して表示
print("=" * 50)
print("参加者別スコア統計")
print("=" * 50)

for name in sorted(scores_by_person.keys()):
    scores = scores_by_person[name]
    average = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    
    print(f"\n【{name}】")
    print(f"  平均点: {average:.2f}点")
    print(f"  最高点: {max_score}点")
    print(f"  最低点: {min_score}点")
    print(f"  受験回数: {len(scores)}回")

print("\n" + "=" * 50)

