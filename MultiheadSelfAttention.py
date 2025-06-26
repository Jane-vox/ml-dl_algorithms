import torch.nn as nn
import torch
import numpy as np
import math


class MultiheadSelfAttention(nn.Module):
    def __init__(self, n_head, hidden_dim, dropout=0.1):
        super().__init__()
        '''
        Multi-head Attention(MHA)
        '''
        self.n_head = n_head
        self.hidden_dim = hidden_dim
        self.head_dim = hidden_dim // n_head

        self.q_proj = nn.Linear(hidden_dim, hidden_dim)
        self.k_proj = nn.Linear(hidden_dim, hidden_dim)
        self.v_proj = nn.Linear(hidden_dim, hidden_dim)
        self.attn_drop = nn.Dropout(dropout)
        self.output_proj = nn.Linear(hidden_dim, hidden_dim)  # 输出线性层，将n_head个子空间映射为统一的空间


    def forward(self, x, attention_mask=None):
        batch_size, seq_len, hidden_dim = x.shape
        q = self.q_proj(x)
        k = self.k_proj(x)
        v = self.v_proj(x)
        # q,k,v shape: (batch, seq_len, hidden_dim)

        # 先扩展维度，再转换 seq_len和 self.n_head维度
        q = q.view(batch_size, seq_len, self.n_head, self.head_dim).transpose(1, 2)
        k = k.view(batch_size, seq_len, self.n_head, self.head_dim).transpose(1, 2)
        v = v.view(batch_size, seq_len, self.n_head, self.head_dim).transpose(1, 2)
        # q,k,v shape (batch_size, n_head, seq_len, head_dim)

        attn_weight = torch.matmul(q, k.transpose(-1, -2)) / math.sqrt(self.head_dim)  # 注意是self.head_dim

        if attention_mask is not None:
            attn_weight = attn_weight.masked_fill(attention_mask == 0, -1e9)

        attn_weight = torch.softmax(attn_weight, dim=-1)

        attn_weight = self.attn_drop(attn_weight)

        output = torch.matmul(attn_weight, v)  # output shape (batch, n_head, seq_len, head_dim)
        output = output.transpose(1, 2).contiguous().view(batch_size, seq_len, self.hidden_dim)
        # output shape (batch_size, seq_len, self.hidden_dim)

        output = self.output_proj(output)
        return output

n_head = 4
hidden_dim = 64
dropout = 0.1
batch = 2
seq_len = 4
mask = None
x = torch.randn(batch, seq_len, hidden_dim)
MHA = MultiheadSelfAttention(n_head, hidden_dim, dropout)
out = MHA(x, mask)
print(out.shape)
loss = out.mean()
loss.backward()


