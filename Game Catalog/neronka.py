import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, GRU, Dense, SpatialDropout1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam

# Загрузка CSV
data = pd.read_csv(r'C:\Diplom\games_catalog.csv')

# Предположим, что ответы на вопросы находятся в колонке 'responses', а целевая переменная в 'target'
X = data['responses'].values
y = data['target'].values

# Преобразуем текстовые данные в последовательности индексов слов
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(X)
X_seq = tokenizer.texts_to_sequences(X)

# Подготовка данных (добавление padding)
X_seq = pad_sequences(X_seq, padding='post', maxlen=100)

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X_seq, y, test_size=0.2, random_state=42)

# Создание модели LSTM/GRU
model = Sequential([
    Embedding(input_dim=10000, output_dim=128, input_length=X_seq.shape[1]),
    SpatialDropout1D(0.2),
    LSTM(100, dropout=0.2, recurrent_dropout=0.2),  # Для LSTM
    # GRU(100, dropout=0.2, recurrent_dropout=0.2),  # Для GRU (закомментировано)
    Dense(1, activation='sigmoid')  # Для бинарной классификации, для регрессии используйте 'linear'
])

# Компиляция модели
model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])  # Для классификации
# model.compile(optimizer=Adam(), loss='mse', metrics=['mae'])  # Для регрессии (если необходимо)

# Обучение модели
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Оценка модели
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f'Test accuracy: {test_acc}')
