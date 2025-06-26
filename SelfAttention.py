import torch.nn as nn
import torch
import numpy as np
import math


class SelfAttention(nn.Module):
    def __init__(self, hidden_dim, dropout=0.1):
        super().__init__()

        self.hidden_dim = hidden_dim
        self.q_proj = nn.Linear(hidden_dim, hidden_dim)
        self.k_proj = nn.Linear(hidden_dim, hidden_dim)
        self.v_proj = nn.Linear(hidden_dim, hidden_dim)

        self.attn_drop = nn.Dropout(dropout)
        # self.output_proj = nn.Linear(hidden_dim, hidden_dim)

    def forward(self, x, attention_mask=None):
        q = self.q_proj(x)
        k = self.k_proj(x)
        v = self.v_proj(x)
        # q,k,v shape (batch, seq_len, hidden_dim)

        attn_weight = torch.matmul(q, k.transpose(1, 2))

        if attention_mask is not None:
            attn_weight = attn_weight.masked_fill(attention_mask == 0, -1e9)

        attn_weight = torch.softmax(attn_weight / math.sqrt(self.hidden_dim), dim=-1)
        attn_weight = self.attn_drop(attn_weight)
        output = torch.matmul(attn_weight, v)

        return output
