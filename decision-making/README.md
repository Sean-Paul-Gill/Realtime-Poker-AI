**The decision making function is currently under-development. The plan is to carry it as follows:**

Take a pre-trained poker model and run 3 XGBoost Classifiers (raise, call, fold) on this data-set. These classifers will be pre-trained and therefore not much computation will be needed on-the-fly. 

After looking at the pre-trained model, we will evaluate our decision based on the current gameplay state. The current gameplay state is what has happened in the previous n rounds. 
Through using the pre-trained model and the on-the-fly classifiers, we can make appropriate moves when Anomaly plays occur. 
