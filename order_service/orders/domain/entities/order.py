class Order:
    def __init__(
        self,
        id,
        usuario_id,
        produto_id,
        produto_nome,
        produto_preco,
        adicionais,
        entrega,
        pagamento,
        subtotal,
        desconto,
        taxa_entrega,
        valor_total,
        criado_em=None,
    ):
        self.id = id
        self.usuario_id = usuario_id
        self.produto_id = produto_id
        self.produto_nome = produto_nome
        self.produto_preco = produto_preco
        self.adicionais = adicionais
        self.entrega = entrega
        self.pagamento = pagamento
        self.subtotal = subtotal
        self.desconto = desconto
        self.taxa_entrega = taxa_entrega
        self.valor_total = valor_total
        self.criado_em = criado_em