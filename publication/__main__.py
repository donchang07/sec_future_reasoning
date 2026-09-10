"""python -m publication: publish pending results without invoking prediction."""
import json
from datetime import datetime,timezone
from pathlib import Path
from uuid import uuid4
from forward_ops.store import Store
from .publisher import publish


def main():
    root=Path(__file__).resolve().parents[1];state=root/'artifacts/local/publication';state.mkdir(parents=True,exist_ok=True)
    marker=state/'active.lock'
    try:
        with marker.open('x') as stream:stream.write(str(datetime.now(timezone.utc)))
    except FileExistsError:raise RuntimeError('Another publisher active; inspect publisher lock')
    try:
        result=publish(root,Store(root/'artifacts/local/forward-evaluation-v1'))
    except Exception as exc:
        result={'status':'error','error':str(exc)}
        raise
    finally:
        with (state/(str(uuid4())+'.json')).open('x',encoding='utf-8') as stream:
            json.dump({'at':datetime.now(timezone.utc).isoformat(),**result},stream,ensure_ascii=False)
        marker.unlink()
    if __import__('sys').stdout is not None:print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
