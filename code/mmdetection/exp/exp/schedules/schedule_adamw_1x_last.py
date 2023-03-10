optimizer = dict(
    type="AdamW",
    lr=0.0001,
    betas=(0.9, 0.999),
    weight_decay=0.05,
    paramwise_cfg=dict(
        custom_keys={
            "absolute_pos_embed": dict(decay_mult=0.0),
            "relative_position_bias_table": dict(decay_mult=0.0),
            "norm": dict(decay_mult=0.0),
        }
    ),
)
optimizer_config = dict(grad_clip=None)
lr_config = dict(policy="poly", power=0.9, min_lr=1e-4, by_epoch=False)
runner = dict(type="EpochBasedRunner", max_epochs=5)
