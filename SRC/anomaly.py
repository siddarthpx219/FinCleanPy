from sklearn.ensemble import IsolationForest
from keras.models import Model
from keras.layers import Input, Dense
from sklearn.preprocessing import StandardScaler
import numpy as np

def remove_outliers(df, method="isolation_forest"):
    if method == "isolation_forest":
        iso = IsolationForest()
        mask = iso.fit_predict(df) == 1
        return df[mask]
    elif method == "autoencoder":
        scaler = StandardScaler()
        df_scaled = scaler.fit_transform(df)
        input_dim = df.shape[1]
        input_layer = Input(shape=(input_dim,))
        encoded = Dense(64, activation='relu')(input_layer)
        decoded = Dense(input_dim, activation='linear')(encoded)
        autoencoder = Model(inputs=input_layer, outputs=decoded)
        autoencoder.compile(optimizer='adam', loss='mse')
        autoencoder.fit(df_scaled, df_scaled, epochs=10, batch_size=32, verbose=0)
        recon = autoencoder.predict(df_scaled)
        loss = np.mean((df_scaled - recon)**2, axis=1)
        return df[loss < np.percentile(loss, 95)]
