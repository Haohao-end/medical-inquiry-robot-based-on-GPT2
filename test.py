# logit = logit[..., :-1, :].contiguous().view(-1, logit.size(-1))
# labels = target[..., 1:].contiguous().view(-1)

import torch
pred = torch.randn(2, 3, 4) # 模型预测结果

labels = torch.randn(2, 3)
print(labels[:, 1:])
new_labels = labels[:, 1:].contiguous().view(-1)
print(new_labels.shape)
# logit = pred[..., :-1, :]
logit = pred[:, :-1, :]
new_logit  = logit.contiguous().view(-1, pred.size(-1))
print(logit.shape)
print(new_logit.shape)
