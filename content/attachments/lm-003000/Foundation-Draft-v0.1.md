# T 是 T，T 不是 T
## 多重同一性符號學與符號身份動力學的初步框架

**英文題名：** *When T Is T and Is Not T: A Preliminary Framework for Multi-Identity Semiotics and Symbolic Identity Dynamics*  
**系列：**《T 的九問：符號身份、生成、命名與持續》Paper 01  
**版本：** v0.1 系列封裝重建版  
**日期：** 2026-08-12  
**作者：** Neo.K、Aletheia（AI 協作）

---

## 摘要

本文從：

\[
T\text{ 是 }T
\]

與：

\[
T\text{ 不是 }T
\]

這組表面矛盾出發，提出多重同一性符號學（Multi-Identity Semiotics, MIS）與符號身份動力學（Symbolic Identity Dynamics, SID）。

核心主張是：

\[
\boxed{
\operatorname{Same}(T_i,T_j)
}
\]

在複雜符號身份問題中通常不是充分定義的問題。更完整形式應為：

\[
\boxed{
T_i\equiv_{\alpha,A,c,t}T_j,
}
\]

其中 \(\alpha\) 指定 identity relation，\(A\) 是判定主體，\(c\) 是 context / namespace，\(t\) 是時間。

因此完全可能：

\[
T_i\equiv_G T_j
\]

但：

\[
T_i\not\equiv_X T_j.
\]

也就是「字形相同」與「底層狀態不同」同時成立，而不構成同一命題的直接矛盾。

---

# 1. 多重同一性

定義一族 identity relations：

\[
\mathfrak E
=
\{
\equiv_G,
\equiv_\tau,
\equiv_X,
\equiv_R,
\equiv_N,
\equiv_O,
\equiv_H,
\equiv_C,
\equiv_T
\}.
\]

分別代表：

- glyph；
- type；
- internal state；
- referent；
- naming；
- operation；
- history；
- context；
- temporal identity。

所以：

\[
\boxed{
\text{Same Glyph}
\not\Rightarrow
\text{Same Identity}.
}
\]

反方向：

\[
\boxed{
\text{Different Glyph}
\not\Rightarrow
\text{Different Identity}.
}
\]

---

# 2. Identity Profile

一次具體符號存在可以寫成：

\[
\boxed{
\mathfrak T_i
=
(
\tau_i,g_i,x_i,r_i,n_i,o_i,h_i,c_i,t_i
).
}
\]

因此 T 不是只有字形，而是一個可被投影成 T 的多層身份物件。

---

# 3. T 是 T

如果：

\[
T_1,T_2
\]

都是同一 type 的兩個 token：

\[
T_1\equiv_\tau T_2
\]

但：

\[
T_1\neq_{\mathrm{token}}T_2.
\]

因此自然語言的「它們都是 T」往往已經包含 identity relation 的切換。

---

# 4. T 不是 T

若：

\[
G(T_1)=G(T_2)=T
\]

但：

\[
X(T_1)\neq X(T_2),
\]

則：

\[
\boxed{
T_1\equiv_GT_2
\land
T_1\not\equiv_XT_2.
}
\]

本文稱之為 Multi-Identity Divergence。

---

# 5. Identity Indexing Principle

任何複雜身份主張：

\[
x=y
\]

都應允許展開成：

\[
\boxed{
x\equiv_{\alpha,A,c,t}y.
}
\]

這不是否定數學等號，而是避免自然語言中的「同一」把不同 identity relation 壓成單一符號。

---

# 6. Identity Distance

可以建立 identity-distance vector：

\[
\boxed{
\mathbf d_I(T_i,T_j)
=
(
d_G,d_\tau,d_X,d_R,d_N,d_O,d_H,d_C,d_T
).
}
\]

所以兩個 T 可以在一個維度距離為 0，在另一維度差異巨大。

---

# 7. Being T / Being Called T / Becoming T

本文先提出三分：

\[
\boxed{
\text{Being T}
\neq
\text{Being Called T}
\neq
\text{Becoming T}.
}
\]

它們分別在後續 Paper 04–05 展開。

---

# 8. Persistence

若：

\[
T_t
\rightarrow
T_{t+1}
\]

發生狀態變化：

\[
X(T_t)\neq X(T_{t+1}),
\]

仍可能在歷史身份下：

\[
T_t\equiv_HT_{t+1}.
\]

所以：

\[
\boxed{
\text{Persistence}
\neq
\text{No Change}.
}
\]

---

# 9. Identity Recurrence

若：

\[
T_0
\rightarrow
X
\rightarrow
T_2,
\]

最後重新滿足某 identity relation，可以形成：

\[
\boxed{
\text{Identity Recurrence / Re-identification}.
}
\]

但這是否為原 numerical identity，必須依 gap、lineage 與 policy 判斷。

---

# 10. 單符號極限

考慮：

\[
\Gamma_n
=
T_1T_2\cdots T_n
\]

且：

\[
\forall i,\quad G(T_i)=T.
\]

可見 alphabet：

\[
\mathcal A_G=\{T\}.
\]

因此在固定 glyph 模型下：

\[
H(G)=0.
\]

但如果底層 identity states 非退化：

\[
H(Z\mid G=T)>0.
\]

所以：

\[
\boxed{
\text{Surface Symbol Complexity}
\neq
\text{Latent Identity Complexity}.
}
\]

---

# 11. 系列核心問題

本文最終把：

> T 到底是不是 T？

改寫成：

\[
\boxed{
\text{Same under which relation, for which observer, in which context, at which time?}
}
\]

後續七篇皆是對這個問題的展開。
